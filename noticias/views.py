from django.shortcuts import render
from .models import Noticias

# Create your views here.
def noticias(request):
    pegaNoticias = Noticias.objects.all().order_by('dataNoticia')
    return render(request,'noticias.html',{'pegaNoticias':pegaNoticias})

