
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPageView, name='prescriber_index'),
    path('search/', views.searchPageView, name='search'),
    path('search/<entity>/', views.searchPageView, name='search_entity'),
    path('details/<int:npi>/', views.detailsPageView, name='details'),
    path('recommend/<entity>/', views.recommendPageView, name='recommend'),

]
