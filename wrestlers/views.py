from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
# from django.template import loader

# Create your views here.
from .models import Wrestler

def index(request):
    latest_wrestlers_list = Wrestler.objects.order_by('wins')[:10]
    context = {'latest_wrestlers_list': latest_wrestlers_list}
    return render(request, 'wrestlers/index.html', context )

def detail(request, name):
    wrestler = get_object_or_404(Wrestler, name=name)
    return render(request, 'wrestlers/detail.html', {'wrestler': wrestler})
