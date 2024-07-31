from django.urls import path
from my_app import views

urlpatterns = [
    path('getProfiles', views.getProfiles, name='getProfiles'),
    path("getProfilesV2", views.getProfilesV2, name='getProfilesV2'),
    path('create', views.create, name='create'),
    path('with-fetch', views.with_fetch, name='with-fetch'),
    path('', views.index, name='index'),
]