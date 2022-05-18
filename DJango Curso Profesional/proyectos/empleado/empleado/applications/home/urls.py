from django.contrib import admin
from django.urls import path

# Importamos views
from . import views

urlpatterns = [
    path('prueba/', views.PruebaView.as_view()),
]

