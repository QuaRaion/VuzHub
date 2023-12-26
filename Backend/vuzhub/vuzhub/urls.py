"""
Definition of urls for Сайт.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls,),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('exams/', views.exams, name='exams'),
    path('universities/', views.universities, name='universities'),
    path('specialties/', views.specialtiespage, name='specialties'),
    path('calendar/', views.calendar, name='calendar'),
    path('home', views.home, name='home'),
    path('exams', views.exams, name='exams'),
    path('universities', views.universities, name='universities'),
    path('specialties', views.specialtiespage, name='specialties'),
    path('calendar', views.calendar, name='calendar'),
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)