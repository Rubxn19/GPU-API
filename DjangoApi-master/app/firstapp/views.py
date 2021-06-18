# Create your views here.
#IMPORT models

#IMPORT LIBRARIRES/FUNCTIONS
from typing import Text
#from typing_extensions import Required
from django.forms import fields
from django.shortcuts import redirect, render , HttpResponse
from django.http import JsonResponse
import json
from django.utils import html
import requests
#IMPORT DJANGO PASSWORD HASH GENERATOR AND COMPARE
from django.contrib.auth.hashers import make_password, check_password
from .models import Dogs,Types, Gpus
from django import forms
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import json

#check_password(noHashPassword,HashedPassword) this funcion validate if the password match to the hash


class GpuForm(forms.ModelForm):
    class Meta:
        model = Gpus #model es igual al modelo del archivo models.py
        fields = [
            'model',
            'brand',
            'chip',
            'retail_price'
        ]
        labels = { 
            'model' : 'Modelo', 
            'brand' : 'Marca',
            'chip' : 'Chip',
            'retail_price' : 'Precio'
        }
        widgets = {
            'model' : forms.TextInput(attrs={'required': True}), #Para validar los campos del form
            'brand' : forms.TextInput(attrs={'required': True}),
            'chip' : forms.TextInput(attrs={'required': True}),
            'retail_price' : forms.TextInput(attrs={'required': True})
        }
    


def vista(request):

    if request.method == 'GET':

        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = list(Gpus.objects.all().values())
      
        cuantos = len(responseData['data']);

        return render(request, 'clase.html', {'cuantos': cuantos , "Gpus": responseData })

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'

        cuantos = len(responseData['data']);
        return r
  


def dogs(request):

    if request.method == 'GET':

        apikey = request.headers.get('api_key')
        apikey = "33390d09esdioewu0qe0uqu0"
        if apikey is not None:

            if apikey != "33390d09esdioewu0qe0uqu0":
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'API KEY NOT VALID'
                return JsonResponse(responseData, status=400)

            responseData = {}
            responseData['success'] = 'true'
            responseData['key'] = apikey
            responseData['data'] = list(Dogs.objects.all().values())
            return JsonResponse(responseData, status=200)

        responseData = {}
        responseData['success'] = 'false'
        responseData['message'] = 'No api Key'
        return JsonResponse(responseData, status=400)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)


def dogsAdd(request):

    if request.method == 'POST':

        try:
            json_object = json.loads(request.body)
            newDog = Dogs(name=json_object['dog_name'], type_id=json_object['dog_type_id'], color=json_object['dog_color'], size= json_object['dog_size'])
            #INSERT INTO dogs (name, type_id,color,size) values ('Solovino',4,'black','big')
            newDog.save()
            responseData = {}
            responseData['success'] = 'true'
            responseData['message'] = 'Dog inserted'
            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def dogsDelete(request):

    if request.method == 'DELETE':

        try:
            json_object = json.loads(request.body)
            try:
                one_entry = Dogs.objects.get(id=json_object["dog_id"])
            except:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'The dog_id its not valid'
                return JsonResponse(responseData, status=400)
            Dogs.objects.filter(id=json_object["dog_id"]).delete()
            responseData = {}
            responseData['success'] = 'true'
            responseData['message'] = 'The dog has been deleted'
            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)
    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def dogsGet(request):

    if request.method == 'POST':

        try:
            json_object = json.loads(request.body)
            try:
                one_entry = Dogs.objects.get(id=json_object["dog_id"])
            except:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'The dog_id its not valid'
                return JsonResponse(responseData, status=400)
            responseData = {}
            responseData['success'] = 'true'
            responseData['data'] = {}
            responseData['data']['name'] = one_entry.name
            responseData['data']['size'] = one_entry.size
            responseData['data']['color'] = one_entry.color
            responseData['data']['type_id'] = one_entry.type_id

            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)
    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def dogsGetId(request, dogid):

    if request.method == 'GET':

        try:
            one_entry = Dogs.objects.get(id=dogid)
        except:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'The dog_id its not valid'
            return JsonResponse(responseData, status=400)

        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = {}
        responseData['data']['name'] = one_entry.name
        responseData['data']['size'] = one_entry.size
        responseData['data']['color'] = one_entry.color
        responseData['data']['type_id'] = one_entry.type_id

        return JsonResponse(responseData, status=200)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def dogsUpdate(request,dogid):

    if request.method == 'POST':
        try:
            one_entry = Dogs.objects.get(id=dogid)
        except:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'The dog_id its not valid'
            return JsonResponse(responseData, status=400)
        try:
            json_object = json.loads(request.body)
            contador = 0
            #AQUI VA EL CODIGO DEL UPDATE
            try:
                value = json_object["dog_name"]
                Dogs.objects.filter(id=dogid).update(name=json_object["dog_name"])
                contador = contador + 1
            except KeyError:
                responseData = {}

            try:
                value = json_object["dog_size"]
                Dogs.objects.filter(id=dogid).update(size=json_object["dog_size"])
                contador = contador + 1
            except KeyError:
                responseData = {}

            try:
                value = json_object["dog_color"]
                Dogs.objects.filter(id=dogid).update(color=json_object["dog_color"])
                contador = contador + 1
            except KeyError:
                responseData = {}

            try:
                value = json_object["dog_type"]
                Dogs.objects.filter(id=dogid).update(type_id=json_object["dog_type"])
                contador = contador + 1
            except KeyError:
                responseData = {}

            if contador == 0:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'Nada por actualizar'
                return JsonResponse(responseData, status=400)
            else:
                responseData = {}
                responseData['success'] = 'true'
                responseData['message'] = 'Datos actualizados'
                return JsonResponse(responseData, status=200)

        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def types(request):

    if request.method == 'GET':

        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = list(Types.objects.all().values())
        return JsonResponse(responseData, status=200)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

###############################################################

def gpus(request):
    
    if request.method == 'GET':

        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = list(Gpus.objects.all().values())
        return JsonResponse(responseData, status=200)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)



def gpusAdd(request):

    if request.method == 'POST':

        # lo que va en la función get('name') es lo que está en el campo del input 
        newGpu = Gpus(model=request.POST.get('model'), brand=request.POST.get('brand'), chip=request.POST.get('chip'), retail_price= request.POST.get('retail_price'))
        newGpu.save()
        
    return redirect('/')
    

def gpusDelete(request, id):

    if request.method == 'POST':
        #teamdelete = Teams.objects.get(id = iddelete)
        Gpus.objects.filter(id=id).delete()
        
    return redirect('/')
    
def agregar(request):
    form = GpuForm()
    return render(request, "add.html", {'form' : form} )

def editar(request, id):
    gpuedit = Gpus.objects.get(id = id)

    if request.method == 'GET':
        form = GpuForm(instance = gpuedit)
    else:
        form = GpuForm(request.POST, instance = gpuedit)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, "editar.html", {'form' : form, 'id': id})

def eliminar(request, id, gpu): #Solo me manda al html con el id que se va a trabajar
    return render(request, 'eliminar.html', {'id': id, 'gpu':gpu})


# def gpusGet(request):

#     if request.method == 'POST':

#         try:
#             json_object = json.loads(request.body)
#             try:
#                 one_entry = Gpus.objects.get(id=json_object["gpu_id"])
#             except:
#                 responseData = {}
#                 responseData['success'] = 'false'
#                 responseData['message'] = 'The team_id its not valid'
#                 return JsonResponse(responseData, status=400)
#             responseData = {}
#             responseData['success'] = 'true'
#             responseData['data'] = {}
#             responseData['data']['name'] = one_entry.name
#             responseData['data']['country'] = one_entry.country
#             responseData['data']['league'] = one_entry.league
#             responseData['data']['confederation'] = one_entry.confederation

#             return JsonResponse(responseData, status=200)
#         except ValueError as e:
#             responseData = {}
#             responseData['success'] = 'false'
#             responseData['data'] = 'Invalid Json'
#             return JsonResponse(responseData, status=400)
#     else:

#         responseData = {}
#         responseData['success'] = 'false'
#         responseData['mesage'] = 'Wrong Method'
#         return JsonResponse(responseData, status=400)

# def gpusGetId(request, teamid):

    if request.method == 'GET':
       
        try:
            one_entry = Gpus.objects.get(id=teamid)
        except:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'The team_id its not valid'
            return JsonResponse(responseData, status=400)
        
        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = {}
        responseData['data']['name'] = one_entry.name
        responseData['data']['country'] = one_entry.country
        responseData['data']['league'] = one_entry.league
        responseData['data']['confederation'] = one_entry.confederation

        return JsonResponse(responseData, status=200)
      
    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)


# def confederation(request):

#     if request.method == 'GET':

#         responseData = {}
#         responseData['success'] = 'true'
#         responseData['data'] = list(Confederation.objects.all().values())
#         return JsonResponse(responseData, status=200)

#     else:

#         responseData = {}
#         responseData['success'] = 'false'
#         responseData['mesage'] = 'Wrong Method'
#         return JsonResponse(responseData, status=400)


# def editar(request, idedit):
       


  


# def add(request):
#     form = TeamForm()
#     return render(request, "add.html", {'form' : form} )


# def eliminar(request, iddelete, nameteam): #Solo me manda al html con el id que se va a trabajar

    
#     return render(request, 'eliminar.html', {'id': iddelete, 'name':nameteam})




