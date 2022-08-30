import re
from django.shortcuts import render
import random

# Create your views here.
def index(request):
    # 앱 이름의 templates에서 .html 파일 찾기
    return render(request, 'index.html')

def greeting(request):
    foods = ['apple', 'banana', 'coconut',]
    info = {
        'name' : 'Alice',
    }
    context = {
        'foods' : foods,
        'info' : info,
    }
    return render(request, 'greeting.html', context)

def dinner(request):
    foods = ['떡볶이', '햄버거', '치킨', '초밥',]
    pick = random.choice(foods)
    context = {
        'pick' : pick,
        'foods' : foods,
    }
    return render(request, 'dinner.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request, 'catch.html', context)

def hello(request, name):
    context = {
        'name' : name, 
    }
    return render(request, 'hello.html', context)