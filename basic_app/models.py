from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:categorydetail",kwargs={'pk':self.pk})

class Influencer(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    instahandle = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length = 256)
    delivery = models.CharField(max_length=256)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='influencers')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:influencerdetail",kwargs={'pk':self.pk})
