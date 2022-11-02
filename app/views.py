from django.shortcuts import render
import imp
from app.models import *

# Create your views here.

def loc(request):
    L=Location.objects.all()
    d={'locs':L}
    return render(request, 'display_loc.html',d)

def depart(request):
    D=Department.objects.all()
    d={'depart':D}
    return render(request, 'display_depart.html',d)