from django.urls import path
from . import views

urlpatterns = [
    path('delete/<int:id>/', views.delete, name='delete'),
    path('complete/<int:id>/', views.complete, name='complete'),
    path('add/', views.add, name='add'),
    path('', views.list, name='list'),
]