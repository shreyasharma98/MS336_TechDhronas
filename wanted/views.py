from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def submit_info(request):
    return HttpResponse("Submited")