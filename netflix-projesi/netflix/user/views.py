from django.shortcuts import render,redirect
from .form import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def userRegister(request):
    form = UserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,'kayıt başarılı')
            return redirect('login')
    
    context = {
        'form': form,
    }
    
    return render(request, 'register.html',context)

def userLogin(request):
    if request.method == 'POST':
        username =request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'giriş başarılı')
            return redirect('profiles')
        else:
            return redirect('login')
    
    return render(request, 'login.html')
def profiles(request):
    profiller = Profiles.objects.filter(owner=request.user)
    context ={
        'profiller':profiller
    }
    return render(request, 'browse.html',context)

def createProfil(request):
    form = ProfilForm()
    profiller = Profiles.objects.filter(owner=request.user)
    if request.method == 'POST':
        if len(profiller) < 5:
          form=ProfilForm(request.POST,request.FILES)
        if form.is_valid():
            profil = form.save(commit=False)
            profil.owner = request.user
            profil.save()
            messages.success(request,'profil oluşturuldu')
            return redirect('profiles')
    
    context = {
        'form': form
    }
    return render(request, 'create.html',context)
