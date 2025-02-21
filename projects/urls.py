from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<int:primary_key>/', views.project, name='project'),
]