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
    image_url = models.URLField(default="https://media.istockphoto.com/vectors/no-image-vector-symbol-missing-available-icon-no-gallery-for-this-vector-id1128826884?k=20&m=1128826884&s=612x612&w=0&h=3GMtsYpW6jmRY9L47CwA-Ou0yYIc5BXRQZmcc81MT78=")
    # category = models.ForeignKey(Category, on_delete= models.DO_NOTHING, related_name="listings")


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    listing = models.ForeignKey(Listing, on_delete= models.CASCADE, related_name="comments")
    content = models.CharField(max_length=140)

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= "bids")
    listing = models.ForeignKey(Listing, on_delete= models.CASCADE, related_name="bids")
    price = models.IntegerField()

