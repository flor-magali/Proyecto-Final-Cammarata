from django.shortcuts import render

def index(request):
    return render(request, "AppPagweb/index.html")

def usuario(request):
      return render(request, "AppPagweb/usuario.html")

def postear(request):
      return render(request, "AppPagweb/postear.html")

def adoptame(request):
      return render(request, "AppPagweb/adoptame.html")