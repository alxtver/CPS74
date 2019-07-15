from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.ind, name='index'),
    path('components/', views.components_list, name='components_list'),
    path('components/new/', views.components_new, name='components_new'),
    path('arrival/', views.arrival, name='arrival'),
    path('search/', views.search, name='search'),
    path('comp/', views.comp, name='comp'),
]