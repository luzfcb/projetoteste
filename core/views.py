from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Empresta

class EmprestaListView(ListView):
    model = Empresta
    template_name = 'core/base.html'


empresta_list_view = EmprestaListView.as_view()
