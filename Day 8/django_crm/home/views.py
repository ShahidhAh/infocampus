from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def first(request):
    return HttpResponse("First Page")

def second(request):
    return HttpResponse("Second Page")