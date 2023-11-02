from django.urls import path
from . import views

urlpatterns = [
path('api/hotels/', views.list_hotels, name='list-hotels'),
]
