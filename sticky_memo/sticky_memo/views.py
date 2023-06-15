from django.shortcuts import HttpResponse, render

def my_home(request):
    return HttpResponse("<h1>hello world!</h1>")

def index(request):
    return render(request,"index.html")