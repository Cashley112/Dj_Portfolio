from django.contrib import admin
from django.urls import path
from django.urls import path
from . import views


app_name = "projects"

urlpatterns = [
    path('', views.all_projects, name='all_projects'),
    path('<int:pk>', views.project_detail, name='project_detail'),
    path('contact', views.contact_page, name='contact_page'),
]