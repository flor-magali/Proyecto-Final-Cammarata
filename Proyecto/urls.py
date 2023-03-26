"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppPagweb.views import (index, usuario, adoptame, agregar_usuario, agregar_post, agregar_adopcion, buscar_animal,buscar)
from AppPagweb.views import ( PostCreate, PostDelete, PostSearch, PostUpdate, PostDetail,PostList, Login, SignUp, Logout, PostMineList)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name = "Inicio"),
    path('usuario/', usuario, name="Usuario"),
    path('adoptame/', adoptame, name="Adoptame"),
    path('usuario/agregar',agregar_usuario, name='agregar-usuario'),
    path('postear/agregar',agregar_post, name='agregar-post'),
    path('adoptame/agregar',agregar_adopcion, name='agregar-adopcion'),
    path('buscar',buscar, name='buscar'),
    path('buscar/animal',buscar_animal, name='buscar-animal'),
    path('postear/', PostCreate.as_view(), name="Postear"),
    path('post/list', PostList.as_view(), name="post-list"),
    path('post/<pk>/detail', PostDetail.as_view(), name="post-detail"),
    path('post/<pk>/update', PostUpdate.as_view(), name="post-update"),
    path('post/<pk>/delete', PostDelete.as_view(), name="post-delete"),
    path('post/search', PostSearch.as_view(), name="post-search"),
    path('login/', Login.as_view(), name="login"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('logout/', Logout.as_view(), name="logout"),
    path('post/list/mine', PostMineList.as_view(), name="post-mine"),

]

