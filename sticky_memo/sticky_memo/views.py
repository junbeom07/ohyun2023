from django.shortcuts import HttpResponse

def my_home(request):
    return HttpResponse("<h1>hello world!</h1>")