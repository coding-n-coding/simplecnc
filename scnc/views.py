from django.shortcuts import render, HttpResponse, redirect
from scnc.models import Cnc
from django.core.paginator import Paginator, EmptyPage

# Create your views here.

def home(request):
    name = 'Ravinder Singh'
    data = {
        'name':name,
    }
    return render(request, 'hm.html',data)

def cnc(request):
    
    cncData = Cnc.objects.all().order_by('-date')
    if request.method == "GET":
        code = request.GET.get("CncData")
        if code != None:
            cncData = Cnc.objects.filter(
                topic__icontains=code).order_by('-date')
    name = 'Ravinder Singh'
    data = {
        'cncData': cncData,
        'name':name,
    }
    
    return render(request, "cd.html", data)
