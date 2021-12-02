from django.urls import path
from . import views

urlpatterns = [
    path('', views.noticias, name='notiias'),
]