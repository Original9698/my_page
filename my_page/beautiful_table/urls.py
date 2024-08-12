from django.urls import path, register_converter
from beautiful_table import views


urlpatterns = [
    path('', views.main_menu, name='table'),
]