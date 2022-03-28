from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=64)

class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=140)
    price = models.IntegerField()
    watchers = models.ManyToManyField(User, blank=True, related_name="watchlist")
    image_url = models.URLField()

    def __str__(self):
        return f"{self.title} ({self.id})"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    listing = models.ForeignKey(Listing, on_delete= models.CASCADE, related_name="comments")
    content = models.CharField(max_length=140)

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= "bids")
    listing = models.ForeignKey(Listing, on_delete= models.CASCADE, related_name="bids")
    price = models.IntegerField()

