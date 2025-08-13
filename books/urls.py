from django.contrib import admin
from django.urls import path
from . import views


app_name = "books"
urlpatterns = [
    path("new/", views.new, name="new"),
    path("", views.index, name="index"),
]
