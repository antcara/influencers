from django.urls import path, re_path
from basic_app import views
from django.urls import reverse_lazy
from django.views.generic import CreateView

app_name = 'basic_app'

urlpatterns = [

    path('influencer_list/',views.InfluencerListView.as_view(),name='influencerlist'),
    re_path('influencer/(?P<pk>\d+)/$',views.InfluencerDetailView.as_view(),name='influencerdetail'),
    path('create_influencer/',views.InfluencerCreateView.as_view(),name='createinfluencer'),
    re_path(r'^updateprofile/(?P<pk>\d+)/$',views.InfluencerUpdateView.as_view(),name='updateinfluencer'),
    re_path(r'^deleteprofile/(?P<pk>\d+)/$',views.InfluencerDeleteView.as_view(),name='deleteinfluencer'),

    path('categories_list/',views.CategoryListView.as_view(),name='categorylist'),
    re_path('category/(?P<pk>\d+)/$',views.CategoryDetailView.as_view(),name='categorydetail'),
    path('create/',views.CategoryCreateView.as_view(),name='create'),
    re_path(r'^update/(?P<pk>\d+)/$',views.CategoryUpdateView.as_view(),name='update'),
    re_path(r'^delete/(?P<pk>\d+)/$',views.CategoryDeleteView.as_view(),name='delete'),

    path('race_list/',views.RaceListView.as_view(),name='racelist'),
    re_path('race/(?P<pk>\d+)/$',views.RaceDetailView.as_view(),name='racedetail'),

    path('gender_list/',views.GenderListView.as_view(),name='genderlist'),
    re_path('gender/(?P<pk>\d+)/$',views.GenderDetailView.as_view(),name='genderdetail'),

    path('location_list/',views.LocationListView.as_view(),name='locationlist'),
    re_path('location/(?P<pk>\d+)/$',views.LocationDetailView.as_view(),name='locationdetail'),

]
