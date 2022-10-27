from basic_api import views
from django.urls import path

urlpatterns = [
    path('api', views.info_list)
]