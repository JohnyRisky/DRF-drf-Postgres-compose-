from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [
    path('', TasksListView.as_view(), name='index'),
    path('<int:pk>/', TaskAddUpdateDeleteView.as_view(), name='task_pk'),
    path('crawl/', parse_hub, name='crawl'),
]