from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.handlelogin,name='login'),
    path('logout/',views.handlelogout,name='logout'),
]
