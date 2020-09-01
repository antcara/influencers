from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256,blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:categorydetail",kwargs={'pk':self.pk})

class Race(models.Model):
    name = models.CharField(max_length=256, blank=True,default='1')

    def __str__(self):
            return self.name

    def get_absolute_url(self):
        return reverse("basic_app:racedetail",kwargs={'pk':self.pk})


class Gender(models.Model):
    name = models.CharField(max_length=256, blank=True,default='1')

    def __str__(self):
            return self.name

    def get_absolute_url(self):
        return reverse("basic_app:genderdetail",kwargs={'pk':self.pk})


class Location(models.Model):
    name = models.CharField(max_length=256, blank=True,default='1')

    def __str__(self):
            return self.name

    def get_absolute_url(self):
        return reverse("basic_app:locationdetail",kwargs={'pk':self.pk})


class Influencer(models.Model):
    name = models.CharField(max_length=256,blank=True)
    surname = models.CharField(max_length=256,blank=True)
    link = models.CharField(max_length=256)
    age = models.PositiveIntegerField(null=True,blank=True)
    phone = models.CharField(max_length=15,blank=True)
    email = models.EmailField(max_length = 256,blank=True)
    delivery = models.CharField(max_length=256,blank=True)
    category = models.ManyToManyField(Category,related_name='influencers')
    race = models.ForeignKey(Race,on_delete=models.CASCADE,blank=True,null=True,related_name='influencers')
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE,blank=True,null=True,related_name='influencers')
    location = models.ForeignKey(Location,on_delete=models.CASCADE,blank=True,null=True,related_name='influencers')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:influencerdetail",kwargs={'pk':self.pk})
