"""TaCar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.dom.minidom import Document
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from Core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("acounts/", include('django.contrib.auth.urls')),
    path("acounts/registrar", Registrar.as_view(), name="Registrar"),
    path("", home, name="url_principal"),

    path("cadastro_cliente/", cadastro_cliente, name="Cadstro Cliente"),
    path("cadastro_veiculo/", cadastro_veiculo, name="Cadstro Veiculo"),
    path("cadastro_fabricante/", cadastro_fabricante, name="Cadastro Fabricante"),
    path("cadastro_rotativo/", cadastro_rotativo, name="Cadastro Rotativo"),
    path("cadastro_mensalista/", cadastro_mensalista, name="Cadastro Mensalista"),

    path("lista_clientes/", lista_clientes, name="Lista_Clientes"),
    path("lista_veiculos/", lista_veiculos, name="Lista Veiculos"),
    path("lista_de_fabricantes/", lista_de_fabricantes, name="Lista Fabricantes"),
    path("lista_de_rotativos/", lista_de_rotativos, name="Lista Rotativos"),
    path("lista_de_precos/", lista_tabela, name="Lista de Preco"),
    path("lista_mensalistas/", lista_mensalista, name="Lista Mensalistas"),
    

    path("altera_cliente/<int:id>/", alterar_cliente, name="Altera Cliente"),
    path("altera_veiculo/<int:id>/", alterar_veiculo, name="Altera Veiculo"),
    path("altera_fabricante/<int:id>/", alterar_fabricante, name="Altera Fabricante"),
    path("altera_mensalista/<int:id>/", alterar_mensalista, name="Alterar Mensalista"),
    path("altera_rotativo/<int:id>/", alterar_rotativo, name="Altera Rotativo"),

    path("exclui_cliente/<int:id>/", exclui_cliente, name="Exclui Cliente"),
    path("exclui_veiculo/<int:id>/", exclui_veiculo, name="Exclui Veiculo"),
    path("exclui_fabricante/<int:id>/", exclui_fabricante, name="Exclui Fabricante"),
    path("exclui_rotativo/<int:id>/", exclui_rotativo, name="Excluir Rotativo"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)