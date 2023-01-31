from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Info
from django.views.generic import ListView

# Create your views here.


class PostList(ListView):
   model = Info
   ordering = '-pk'


def get_runtime(ms):
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

    if hour == 0 and minute == 0 and second == 0:
        result = '0초'
    return result


def get_date(eng):
    eng_split = eng.split(' ')
    month_table = {
        'Jan.': '1월',
        'Feb.': '2월',
        'Mar.': '3월',
        'Apr.': '4월',
        'May.': '5월',
        'Jun.': '6월',
        'Jul.': '7월',
        'Aug.': '8월',
        'Sep.': '9월',
        'Oct.': '10월',
        'Nov.': '11월',
        'Dec.': '12월',
    }
    return f'{eng_split[2]}년 {month_table[eng_split[0]]}월 {eng_split[1]}일 {eng_split[3]} {eng_split[4]}'

def createform(request):
   std = Info()
   std.battery = request.GET['battery']
   std.color = request.GET['color']
   std.runtime = get_runtime(request.GET['runtime'])
   std.firmV = request.GET['firmV']
   # std.date = get_date(request.GET['created_at'])
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

