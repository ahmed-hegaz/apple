from django.shortcuts import render
from .models import Apple, Text

def apple_list(request):
    apple_list = Apple.objects.all
    context = {'apple' : apple_list }
    return render(request,'apple_list.html',context)


def apple_detail(request , id):
    apple_detail = Apple.objects.get(id=id)

    context = {'apple' : apple_detail }
    return render(request,'apple_detail.html',context)