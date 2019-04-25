from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('how_to_use/', views.how_to_use, name='how_to_use'),
    path('how_to_cite/', views.how_to_cite, name='how_to_cite'),
]