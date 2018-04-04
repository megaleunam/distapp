import json
from django.shortcuts import render

from django.http import HttpResponse

from apps.estudiante.models import Estudiante
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def Get_Estudiante(request,cedula):
    #if not request.is_ajax() or request.method != "POST":
    if request.method == "GET":
    	print(cedula)
    	est = Estudiante.objects.filter(cedula=cedula)
    	print(est)
    	if est.exists():
    		estudiante = {'estudiante':{'cedula':est[0].cedula,'nombres': est[0].nombres,'apellidos':est[0].apellidos,
    		    		'celular':est[0].celular,'email':est[0].correo_electronico}}
    	else:
    		estudiante = {'mensaje':'no existe registro'}
    	return HttpResponse(json.dumps(estudiante), content_type="application/json")
    elif request.method == "POST":
    	nuevo = Estudiante()
    	nuevo.cedula = cedula
    	nuevo.nombres = request.GET.get('nombres')
    	nuevo.apellidos= request.GET.get('apellidos')
    	nuevo.celular = request.GET.get('celular')
    	nuevo.correo_electronico= request.GET.get('email')
    	nuevo.save()
    	print(nuevo,nuevo.cedula,nuevo.nombres)
    	return HttpResponse(json.dumps({'mensaje': str('registro guardado')}), content_type="application/json")    	
    elif request.method == "PUT":
    	nuevo = Estudiante.objects.get(cedula=cedula)
    	nombres = request.GET.get('nombres')
    	if request.GET.get('nombres') != None:
    		nuevo.nombres = request.GET.get('nombres')
    	nuevo.apellidos= request.GET.get('apellidos')
    	nuevo.celular = request.GET.get('celular')
    	nuevo.correo_electronico= request.GET.get('email')
    	#nuevo.save()
    	print(nuevo,nuevo.nombres,nuevo.apellidos,nuevo.celular)
    	return HttpResponse(json.dumps({'mensaje': str('registro actualizado')}), content_type="application/json")
    
    return HttpResponse(json.dumps({'mensaje': str('metodo no existe')}), content_type="application/json")

@csrf_exempt
def Lista_Estudiantes(request):
    #if not request.is_ajax() or request.method != "POST":
    if request.method == "GET":
    	estudiantes = Estudiante.objects.all()
    	lista=[]
    	print(estudiantes)
    	i=1
    	if estudiantes.exists():
    		for est in estudiantes:
	    		estudiante = {'N':i,'estudiante':{'cedula':est.cedula,'nombres': est.nombres,'apellidos':est.apellidos,
	    		'celular':est.celular,'email':est.correo_electronico}}
	    		lista.append(estudiante)
	    		i += 1
    	else:
    		lista = [{'mensaje':'no existe registro'}]
    	return HttpResponse(json.dumps(lista), content_type="application/json")
    
    #Categorias.objects.filter(id_categoria=request.POST.get('pk')).update(
     #   descripcion=request.POST.get('categoria')
    #)
    return HttpResponse(json.dumps({'mensaje': str('metodo no existe')}), content_type="application/json")

