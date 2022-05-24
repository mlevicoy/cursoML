from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class PruebaListView(ListView):
    template_name = "home/lista.html"
    # Creamos una variable para poder acceder a la lista
    context_object_name = "listaNumeros"
    # queryset siempre va hacer referencia a una lista
    queryset = ['0', '10', '20', '30']


    
