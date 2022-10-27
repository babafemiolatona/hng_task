from basic_api import views
from django.urls import path

urlpatterns = [
    path('', views.info_list)
]