from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,UpdateView,DeleteView)
from . import models

class IndexView(TemplateView):
    template_name = 'index.html'


#Category classes

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
    fields=('name','surname','instahandle','age','phone','email','delivery','category')
    model=models.Influencer

class InfluencerUpdateView(UpdateView):
    fields = ('name','surname','instahandle','age','phone','email','delivery','category')
    model = models.Influencer


class InfluencerDeleteView(DeleteView):
    model = models.Influencer
    success_url = reverse_lazy("basic_app:influencerlist")
