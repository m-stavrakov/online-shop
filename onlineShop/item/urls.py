from django.urls import path
from . import views

app_name = 'item'

url_patterns = [
    path('<int:pk>/', views.detail, name='detail'),
]