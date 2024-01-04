from django.urls import path
from . import views

# Url configuration for the playground app
urlpatterns = [
    path('', views.index, name='index'),
    path('get_html/', views.get_html, name='get_html'),
]
