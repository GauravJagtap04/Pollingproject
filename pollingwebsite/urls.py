from django.contrib import admin
from django.urls import path,include
from pollingwebsite import views

app_name = "pollingwebsite"
urlpatterns = [
    path('', views.home, name='home'),
]