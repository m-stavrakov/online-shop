from django.urls import path
from . import views

app_name = 'item'

# IMPORTANT: urlpatterns should be spelled exactly like that
urlpatterns = [
    # this is a path; pk is primary key
    path('<int:pk>/', views.detail, name='detail'),
]