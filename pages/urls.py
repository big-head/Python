#pages/urls.py
from django.urls import path
from .views import homePageView
from .views import AboutPagesView #new 2019/05/09

urlpatterns = [
    path('', homePageView, name = 'home'),
    path('about/', AboutPagesView.as_view(), name = 'about') #new 2019/05/09
]