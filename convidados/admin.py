from django.contrib import admin
from .models import Convidado


# testes de importações e registro do admin do django sem muitas alterações, segue o mesmo padrão da versão 2.0
# Register your models here.
admin.site.register(Convidado)

