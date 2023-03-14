from django.urls import path 
from AppPagweb import views

urlpatterns = [
    path('',views.inicio),
    path('cursos',views.cursos, name='Cursos'),
    path('profesores',views.profesores),
    path('estudaintes',views.estudaintes),
]