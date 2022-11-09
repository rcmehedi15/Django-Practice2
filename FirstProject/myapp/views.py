from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("Hello Bangladesh")
    text = {'name': 'Arafat', 'course': 'Django'}
    return render(request, 'index.html', text)
    

def shop(request):
    return HttpResponse("Welcome to Nongare shop")

def add(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    values = val1 + val2


    return render(request, 'result.html', {'result': values})