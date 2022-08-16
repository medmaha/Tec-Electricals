from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='index'),
    path('message/', views.contact, name='message'),
    path('projects/', views.projects, name='projects'),
    path('about-tec/', views.about, name='about'),
]
