from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('inicio', views.index, name='index'),
    #path(r'^estudiante/(?P<id_estudiante>\d+)$',views.Get_Estudiante,name='estudiante')
    url(r'^estudiante/(?P<cedula>\d+)$',views.Get_Estudiante,name='despacho_procesar'),
    url(r'^estudiante/$',views.Lista_Estudiantes,name='lista_estudiantes'),
   
]