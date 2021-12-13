from django.db import models


#
# by me
# testes de crud para os convidados que poderão acessar o sistema e ver todas as células
# para futuras interações os dados do convidado como email, nome e telefone serão coletados.
# Create your models here.
class Convidado(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    telefone = models.CharField(max_length=13)

    def __str__(self):
        return self.nome()

    
