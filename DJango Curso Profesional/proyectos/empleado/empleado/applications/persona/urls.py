
from django.contrib import admin
from django.urls import path

def desdePersona(self):
    print("==================Desde App persona==================")

urlpatterns = [
    path('persona/', desdePersona),
]
