from django.shortcuts import render

# Create your views here.
from django.contrib import auth, messages
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request,"index.html")
