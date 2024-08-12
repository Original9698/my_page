from django.urls import path, register_converter
from horoscope import views as views_h
from horoscope import converters

urlpatterns = [
    path('', views_h.main_menu, name='horoscope-index'),
    path('<int:month>/<int:day>/', views_h.zodiac_view),
    path('<int:sign_zodiac>/', views_h.get_info_about_sign_zodiac_to_number),
    path('<str:sign_zodiac>/', views_h.get_info_about_sign_zodiac, name='horoscope-name'),
]
