from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from math import pi
from django.urls import reverse


# Create your views here.

def get_rectangle_area(request, width: int, height: int):
    # area = width * height
    # return HttpResponse(f'Площадь прямоугольника размером {width}х{height} равна {area}')
    return render(request, 'geometry/rectangle.html')


def get_square_area(request, width: int):
    # area = width * width
    # return HttpResponse(f'Площадь квадрата размером {width}х{width} равна {area}')
    return render(request, 'geometry/square.html')


def get_circle_area(request, radius: int):
    # area = pi * radius ** 2
    # return HttpResponse(f'Площадь круга радиуса {radius} равна {area:.2f}')
    return render(request, 'geometry/circle.html')


def rectangle(request, width, height):
    redirect_url = reverse('rectangle', args=(width, height,))
    return HttpResponseRedirect(redirect_url)


def square(request, width):
    redirect_url = reverse('square', args=(width,))
    return HttpResponseRedirect(redirect_url)


def circle(request, radius):
    redirect_url = reverse('circle', args=(radius,))
    return HttpResponseRedirect(redirect_url)
