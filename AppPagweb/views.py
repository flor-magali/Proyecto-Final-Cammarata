from django.shortcuts import render
from django.http import HttpResponse
from AppPagweb.forms import UsuarioForm, PostearForm, AdoptameForm
from AppPagweb.models import Usuario, Postear, Adoptame
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def index(request):
    return render(request, "AppPagweb/index.html")

def usuario(request):
    context = {
    "form": UsuarioForm(),
    "usuario": Usuario.objects.all(),
     }
    return render(request, "AppPagweb/usuario.html", context)
    

def adoptame(request):
    context = {
    "form": AdoptameForm(),
    "adopcion": Adoptame.objects.all(),
     }
    return render(request, "AppPagweb/adoptame.html",context)

# def postear(request):
#      context = {
#      "form": PostearForm(),
#      "post": Postear.objects.all(),
#       }
#      return render(request, "AppPagweb/postear.html",context)

class PostCreate(CreateView):
     model = Postear
     success_url = reverse_lazy("post-list")
     print("dasdadsdasdaaaefsef")
     fields = '__all__'

class PostList(ListView):
    model = Postear
    context_object_name = "posts"

class PostDetail(DetailView):
    model = Postear
    context_object_name = "post"

class PostUpdate(UpdateView):
    model = Postear
    success_url = reverse_lazy("post-list")
    fields = '__all__'

class PostDelete(DeleteView):
    model = Postear
    context_object_name = "post"
    success_url = reverse_lazy("post-list")

class PostSearch(ListView):
    model = Postear
    context_object_name = "posts"

    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = Postear.objects.filter(Animal__icontains=criterio).all()
        return result



def agregar_usuario(request):
     usuario_form = UsuarioForm(request.POST)
     usuario_form.save()
     context = {
          "form": UsuarioForm(),
          "usuario": Usuario.objects.all(),
     }
     return render(request, 'AppPagweb/usuario.html', context)

def agregar_post(request):
     post_form = PostearForm(request.POST)
     post_form.save()
     context = {
          "form": PostearForm(),
          "post": Postear.objects.all(),
     }
     return render(request, 'AppPagweb/postear_form.html', context)

def agregar_adopcion(request):
     adopcion_form = AdoptameForm(request.POST)
     adopcion_form.save()
     context = {
          "form": AdoptameForm(),
          "adopcion": Adoptame.objects.all(),
     }
     return render(request, 'AppPagweb/adoptame.html', context)

def buscar(request):
    return render(request, "AppPagweb/buscar.html")

def buscar_animal(request):

       print("buscar()")
       if request.GET['Animal']:

            Animal = request.GET['Animal']

            print("buscar() " + Animal)

            post = Postear.objects.filter(Animal__icontains=Animal)

            return render(request, 'AppPagweb/buscar.html', {"post":post, "Animal": Animal})

       else:
            respuesta = "No enviaste datos"

       return HttpResponse(respuesta)
