from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('how_to_use/', views.how_to_use, name='how_to_use'),
    path('how_to_cite/', views.how_to_cite, name='how_to_cite'),
    path('About/', views.About, name='About'),
    path('Summary/', views.Summary, name='Summary'),
    path('Useful/', views.Useful, name='Useful'),
    path('Online/', views.Online, name='Online'),
    path('Tools/', views.Tools, name='Tools'),
    path('Contact/', views.Contact, name='Contact'),
    path('Events/', views.Events, name='Events'),
    path('Announcement/', views.Announcement, name='Announcement'),
    path('FeedBack/', views.FeedBack, name='FeedBack'),
    path('FAQS/', views.FAQS, name='FAQS'),
]
