from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django import forms
from .models import User, Listing, Comment, Bid


class NewListingForm(forms.Form):
    title = forms.CharField(label= "Title", widget= forms.TextInput(attrs={
        'class' : 'form-control',
        'style' : 'width: 400px; margin-bottom: 20px;',
    }))
    
    description = forms.CharField(label= "Description", widget= forms.Textarea(attrs={
        'class' : 'form-control',
        'style' : 'width: 400px; height: 100px; margin-bottom: 20px;',
    }))

    price = forms.IntegerField(label="Price", widget=forms.NumberInput(attrs={
        'class' : 'form-control',
        'style' : 'width: 400px; margin-bottom: 20px;'
    }))

    image_url = forms.CharField(required= False, label= "Image URL", widget= forms.TextInput(attrs={
        'class' : 'form-control',
        'style' : 'width: 400px; margin-bottom: 20px;',
    }))


def index(request):
    return render(request, "auctions/index.html", {
        "listings" : Listing.objects.all(),
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def new_listing(request):
    if request.method == "GET":
        return render(request, "auctions/new_listing.html", {
            "form" : NewListingForm()
        })
    
    #we are expecting new listing here
    title = request.POST["title"]
    description = request.POST["description"]
    price = request.POST["price"]
    if request.POST["image_url"] == "":
        image_url = "https://media.istockphoto.com/vectors/no-image-vector-symbol-missing-available-icon-no-gallery-for-this-vector-id1128826884?k=20&m=1128826884&s=612x612&w=0&h=3GMtsYpW6jmRY9L47CwA-Ou0yYIc5BXRQZmcc81MT78="
    else:
        image_url = request.POST["image_url"]
    
    listing = Listing(
        user=request.user, 
        title=title, 
        description=description, 
        price= price,
        image_url= image_url,
        )

    listing.save()
    return HttpResponseRedirect(reverse("index"))


def listing(request, listing_id):
    if request.method == "GET":
        return render(request, "auctions/listing.html", {
            "listing" : Listing.objects.get(pk=listing_id),
            "comments" : Listing.objects.get(pk=listing_id).comments.all(),
            "watchers" : Listing.objects.get(pk=listing_id).watchers.all(),
        })
    
    elif request.POST["action"] == "comment":
        content = request.POST["comment"]
        user = request.user
        new_comment = Comment(user=user, content= content, listing=Listing.objects.get(pk=listing_id))
        new_comment.save()
        return HttpResponseRedirect(reverse("listing", args=(listing_id,)))

    elif request.POST["action"] == "watchlist-add":
        Listing.objects.get(pk=listing_id).watchers.add(request.user)
        return HttpResponseRedirect(reverse("listing", args=(listing_id,)))
        
    elif request.POST["action"] == "watchlist-remove":
        Listing.objects.get(pk=listing_id).watchers.remove(request.user)
        return HttpResponseRedirect(reverse("listing", args=(listing_id,)))
    
    elif request.POST["action"] == "bid":
        bid= Bid(user=request.user, price=int(request.POST["bid"]), listing=Listing.objects.get(pk=listing_id))
        bid.save()

        current_listing = Listing.objects.get(pk=listing_id)
        current_listing.price = int(request.POST["bid"])
        current_listing.save()
        
        return HttpResponseRedirect(reverse("listing", args=(listing_id, )))




def watchlist(request):
    return render(request, "auctions/watchlist.html", {
        "listings" : User.objects.get(pk=request.user.id).watchlist.all()
    })