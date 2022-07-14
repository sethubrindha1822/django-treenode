from django.forms import forms
from django.shortcuts import redirect, render
from .models import soap , paste
from .forms import soapform , pasteform
# Create your views here.


def menu(request):
    soaps =soap.objects.all()
    pastes = paste.objects.all()
    context = {'soaps':soaps,'pastes':pastes,}
    return render(request, 'menu/index.html', context = context )


def soapdb(request):
    soaps =soap.objects.all()
  
    context = {'soaps':soaps}
    return render(request, 'menu/soapdb.html', context = context )


def pastedb(request):
    pastes = paste.objects.all()
    context = {'pastes':pastes}
    return render(request, 'menu/pastedb.html', context = context )


def add_soap(request):
    form = soapform()
    if request.method == 'POST':
        form = soapform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    return render(request, 'menu/addsoap.html', {'form':form})


def add_paste(request):
    form1 = pasteform()
    if request.method == 'POST':
        form1 = pasteform(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/home')    
    return render(request, 'menu/addpaste.html', {'form1':form1})

def delete_soap(request,id):
    soaps =soap.objects.get(id = id)
    soaps.delete()
    return redirect('/home')


def delete_paste(request,id):
    pastes =paste.objects.get(id = id)
    pastes.delete()
    return redirect('/home')


def update_soap(request,id):
    soaps =soap.objects.get(id = id)
    if request.method == 'POST':
        form1 = pasteform(request.POST, instance=soaps)
        if form1.is_valid():
            form1.save()
            return redirect('/home')  
    return render(request, 'menu/updatesoap.html', {'soaps':soaps})


def update_paste(request,id):
    pastes =paste.objects.get(id = id)
    if request.method == 'POST':
        form1 = pasteform(request.POST , instance=pastes)
        if form1.is_valid():
            form1.save()
            return redirect('/home')    
    return render(request, 'menu/updatepaste.html',{'pastes':pastes})