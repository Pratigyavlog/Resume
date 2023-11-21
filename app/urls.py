from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('projects/',views.projects,name='projects'),
    path('resume/',views.resume,name='resume')
]