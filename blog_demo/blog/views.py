from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def first_post(request):
    return render(request, 'index.html')