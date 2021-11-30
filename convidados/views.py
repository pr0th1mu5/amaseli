from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    cellSearch = request.GET.get('searchCells')
    return render(request,'home.html',{'cellSearch':cellSearch})

def sobre(request):
    return HttpResponse('<h4>Aqui você está na página <em>sobre</em> o amaseli</h4>')

def signup(request):
    email = request.GET.get('emails')
    return render(request,'signup.html',{'email':email})