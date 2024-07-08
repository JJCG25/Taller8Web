from django.shortcuts import render, HttpResponseRedirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.template import loader
from .models import td,persona,ciudad
from .forms import tdForm, registroForm, CiudadForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.


def tiposd(request):
    tipos = td.objects.all()
    template =  loader.get_template('td/tiposd.html')
    context = {'tipos':tipos,}
    return HttpResponse(template.render(context, request))

def create_tiposd(request):
    if request.method == 'POST':

        form = tdForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['nombre']
            description = form.cleaned_data['descripcion']
            td1 = td(nombre = name,descripcion = description)
            td1.save()
            return HttpResponseRedirect(reverse('tiposd'))
    else :
        form = tdForm()
        
    return render(request,'td/create_tiposd.html',{'form':form})
        
def edit_tiposd(request,pk):
    tipodocumento = get_object_or_404(td, pk=pk)
    if request.method == 'POST':

        form = tdForm(request.POST, instance=tipodocumento)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tiposd'))
    else:
        form = tdForm(instance=tipodocumento)

    return render(request, 'td/create_tiposd.html', {'form': form})

def delete_tiposd(request, pk):
    tipodocumento = get_object_or_404(td, pk=pk)
    if request.method == 'POST':
        tipodocumento.delete()
        return HttpResponseRedirect(reverse('tiposd'))
    return render(request, 'td/delete_tiposd.html', {'tipodocumento': tipodocumento})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('tiposd'))
    else:
        form = AuthenticationForm()
    return render(request, 'persona/login.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = registroForm(request.POST)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.password = make_password(form.cleaned_data['password'])
            persona.idtipodocumento = form.cleaned_data['tipodocumento']
            persona.idciudad = form.cleaned_data['lugarResidencia']
            persona.save()
            return HttpResponseRedirect(reverse('login'))  
    else:
        form = registroForm()
    return render(request, 'persona/registro_persona.html', {'form': form})

def ciudades(request):
    ciudades = ciudad.objects.all()
    template = loader.get_template('ciudad/ciudades.html')
    context = {'ciudades': ciudades}
    return HttpResponse(template.render(context, request))

def create_ciudad(request):
    if request.method == 'POST':
        form = CiudadForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ciudades'))
    else:
        form = CiudadForm()
    return render(request, 'ciudad/create_ciudad.html', {'form': form})

def edit_ciudad(request, pk):
    ciudad1 = get_object_or_404(ciudad, pk=pk)
    if request.method == 'POST':
        form = CiudadForm(request.POST, instance=ciudad1)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ciudades'))
    else:
        form = CiudadForm(instance=ciudad1)
    return render(request, 'ciudad/create_ciudad.html', {'form': form})

def delete_ciudad(request, pk):
    ciudad1 = get_object_or_404(ciudad, pk=pk)
    if request.method == 'POST':
        ciudad1.delete()
        return HttpResponseRedirect(reverse('ciudades'))
    return render(request, 'ciudad/delete_ciudad.html', {'ciudad': ciudad1})


