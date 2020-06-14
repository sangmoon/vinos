from django.shortcuts import render
from django.http import HttpResponse
from app.excels import read_terroir_excel


def index(request):
    return HttpResponse("Hello World, It's your app")


def parse_excel(request):
    file_name = request.GET.get('file_name')
    sheet_name = request.GET.get('sheet_name')
    read_terroir_excel(file_name, sheet_name)

    return HttpResponse('all record are parsed!')
