from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Info
from django.views.generic import ListView

# Create your views here.

class PostList(ListView):
   model = Info
   ordering = '-pk'
   paginate_by = 7


def calc_time(ms):
    if ms == 0:
        return 'NULL'

    second = int(int(ms)/1000)
    minute = int(second/60)
    second %= 60
    hour = int(minute/60)
    minute %= 60

    result = ""
    if hour > 0:
        result += str(hour) + '시간 '
    if minute > 0:
        result += str(minute) + '분 '
    if second > 0:
        result += str(second) + '초 '
    return result

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

