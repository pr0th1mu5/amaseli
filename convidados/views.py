from django.shortcuts import render
from django.http import HttpResponse
from .models import Convidado

# by me
# testes de renderizações das páginas e utilização de templates tags feitas com passagem de parâmetros utilizando name's de forms.
# testes dos novos métodos da versão 3 do django
# Create your views here.
def home(request):
    cellSearch = request.GET.get('searchCells')
    convidados = Convidado.objects.all()
    return render(request,'home.html',{'cellSearch':cellSearch,'convidados':convidados})

def sobre(request):
    return HttpResponse('<h4>Aqui você está na página sobre.<em>sobre</em> o amaseli</h4>')

def signup(request):
    email = request.GET.get('emails')
    return render(request,'signup.html',{'email':email})