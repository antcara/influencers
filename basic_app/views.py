from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,UpdateView,DeleteView,FormView)
from . import models

class IndexView(TemplateView):
    template_name = 'index.html'


#Influencer classes:

class InfluencerListView(ListView):
    context_object_name ='influencers'
    model = models.Influencer
    template_name = 'basic_app/influencer_list.html'

class InfluencerDetailView(DetailView):
    context_object_name = 'influencer_details'
    model = models.Influencer
    template_name = 'basic_app/influencer_detail.html'


class InfluencerCreateView(CreateView):
    fields=('name','link','category','location','gender','race')
    model=models.Influencer

class InfluencerUpdateView(UpdateView):
    fields = ('name','surname','link','category','location','gender','race','age','phone','email','delivery')
    model = models.Influencer


class InfluencerDeleteView(DeleteView):
    model = models.Influencer
    success_url = reverse_lazy("basic_app:influencerlist")


class CategoryListView(ListView):
    context_object_name ='categories'
    model = models.Category


class CategoryDetailView(DetailView):
    context_object_name = 'category_details'
    model = models.Category
    template_name = 'basic_app/category_detail.html'

class CategoryCreateView(CreateView):
    fields = ('name','description')
    model = models.Category

class CategoryUpdateView(UpdateView):
    fields = ('name','description')
    model = models.Category
    success_url = reverse_lazy("basic_app:categorylist")


class CategoryDeleteView(DeleteView):
    model = models.Category
    success_url = reverse_lazy("basic_app:categorylist")

class RaceListView(ListView):
    context_object_name ='races'
    model = models.Race

class RaceDetailView(DetailView):
    context_object_name = 'race_details'
    model = models.Race
    template_name = 'basic_app/race_detail.html'


class GenderListView(ListView):
    context_object_name ='genders'
    model = models.Gender

class GenderDetailView(DetailView):
    context_object_name = 'gender_details'
    model = models.Gender
    template_name = 'basic_app/gender_detail.html'


class LocationListView(ListView):
    context_object_name ='locations'
    model = models.Location

class LocationDetailView(DetailView):
    context_object_name = 'location_details'
    model = models.Location
    template_name = 'basic_app/location_detail.html'
