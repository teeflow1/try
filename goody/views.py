from django.shortcuts import render



def home(request):
    return render(request, 'apps/index.html', {})

def property(request):
    return render(request, 'apps/property.html', {})
