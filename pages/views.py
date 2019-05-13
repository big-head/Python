from django.shortcuts import render

#new
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

# pages/view.py
def homePageView(request):
    return HttpResponse('Hello World !')

# 09/05/2019 new    
class HomePageView(TemplateView):
    templates_name = 'home.html'

class AboutPagesView(TemplateView):
    template_name = 'about.html'