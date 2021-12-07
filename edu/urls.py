from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('facts', views.facts, name='facts'),
    path('resources', views.resources, name='resources'),
    path('resources/<int:id>', views.resources, name='specific_resource'),
    path('contact', views.contact, name='contact'),
    path('community', views.community, name='community'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]
