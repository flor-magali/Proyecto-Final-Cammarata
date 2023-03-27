from django.shortcuts import render
from AppPagweb.models import Postear, Profile
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def index(request):
    return render(request, "AppPagweb/index.html")

class PostCreate(LoginRequiredMixin, CreateView):
     model = Postear
     success_url = reverse_lazy("post-list")
     print("dasdadsdasdaaaefsef")
     fields = '__all__'

class PostList(ListView):
    model = Postear
    context_object_name = "posts"

class PostMineList(LoginRequiredMixin, PostList):
    def get_queryset(self):
        return Postear.objects.filter(publisher=self.request.user.id).all()

class PostDetail(DetailView):
    model = Postear
    context_object_name = "post"

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Postear
    success_url = reverse_lazy("post-list")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        post_id =  self.kwargs.get("pk")
        return Postear.objects.filter(publisher=user_id, id=post_id).exists()

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Postear
    context_object_name = "post"
    success_url = reverse_lazy("post-list")

    def test_func(self):
        user_id = self.request.user.id
        post_id =  self.kwargs.get("pk")
        return Postear.objects.filter(publisher=user_id, id=post_id).exists()

class PostSearch(ListView):
    model = Postear
    context_object_name = "posts"

    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = Postear.objects.filter(Animal__icontains=criterio).all()
        return result
    
class Login(LoginView):
     next_page=reverse_lazy("post-list")

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('post-list')

class Logout(LogoutView):
    template_name = "registration/logout.html"

    
class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    success_url = reverse_lazy("post-list")
    fields = ['avatar',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ProfileUpdate(LoginRequiredMixin,  UpdateView):
    model = Profile
    success_url = reverse_lazy("post-list")
    fields = ['avatar',]

    def test_func(self):
        return Profile.objects.filter(user=self.request.user).exists()



