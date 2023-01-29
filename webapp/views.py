from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Info
from django.views.generic import ListView

# Create your views here.

class PostList(ListView):
   model = Info
   ordering = '-pk'
   paginate_by = 1


def createform(request):
   std = Info()
   std.battery = request.GET['battery']
   std.color = request.GET['color']
   std.runtime = request.GET['runtime']
   std.firmV = request.GET['firmV']

   std.save()

   return redirect('/')


def signin(request):
    if request.method == "GET":
        return redirect('webapp:index')

    elif request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('webapp:index')
            else:
                return redirect('webapp:index')



def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('webapp:index')

