from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('departments/', views.departments, name='departments'),
    path('departments/applications/', views.applications, name='applications')
]
