from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def main_menu(request):
    main_dict ={

    }
    return render(request,'beautiful_table/table.html', context=main_dict)
