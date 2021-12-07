
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPageView, name='prescriber_index'),
    path('search/', views.searchPageView, name='search'),
    path('search/<entity>/', views.searchPageView, name='search_entity'),
    path('details/<entity>/<int:id>/', views.detailsPageView, name='details'),
    path('recommend/<entity>/', views.recommendPageView, name='recommend'),
    path('predtotpresc/', views.PredTotPrescPageView, name='predtotpresc'),
    path('predprescop/', views.PredPrescOp, name='predprescop'),
    path('showprescribers/', views.showPrescribersPageView, name="showprescribers"),
    path("deleteprescriber/<int:npi>/", views.deletePrescriberPageView, name="deletePrescriber"),
    path("addprescriber/", views.addPrescriberPageView, name="addPrescriber"),
    path('updateprescriber/<int:npi>/', views.updatePrescriberPageView, name="updateprescriber"),
] 
