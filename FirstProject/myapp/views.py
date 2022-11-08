from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    text = {'Name': 'Md Mehedi Hasan', 'Course':'Django'}
    return render(request,'index.html',text)
    
def next(request):
    return HttpResponse("Kire Montu")

