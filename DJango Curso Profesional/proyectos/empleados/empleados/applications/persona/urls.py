from django.contrib import admin
from django.urls import path

def DesdeApps(self):
    print('=================dede la app persona================')

urlpatterns = [
    path('persona/', DesdeApps),
]
