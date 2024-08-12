from django.contrib import admin
from django.urls import path
from week_days import views as views_wd

urlpatterns = [
    path('',views_wd.days_list),
    path('<int:day_info>/', views_wd.weeks_day_info_to_number),
    path('<str:day_info>/', views_wd.weeks_day_info, name= 'days'),
]
