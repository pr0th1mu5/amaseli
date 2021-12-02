"""amaseli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from convidados import views as convidadosViews #convidadosViews é um apelido para ser referenciado no path da url

## Testes de configuração de urls para home e demais páginas utilizando as atualizações e com namespaces.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', convidadosViews.home, name='home'),
    path('sobre/', convidadosViews.sobre, name='sobre'),
    path('signup/', convidadosViews.signup, name='signup'),
]
