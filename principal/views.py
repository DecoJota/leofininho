from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def musicas(request):
    return render(request, 'musicas.html')


def sobre(request):
    return render(request, 'sobre.html')
