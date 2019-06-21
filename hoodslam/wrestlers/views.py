from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, world, this is MOTHERFUCKING HOODSLAM!!")

def wrestler(request, name):
    return HttpResponse("This is the page for %s" % name)

def match(request, match_id):
    #pull fighters from the match and displays a page with the 
    pass
