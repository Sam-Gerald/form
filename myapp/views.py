from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse

def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
