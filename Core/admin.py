from django.contrib import admin
from Core.models import *

# Register your models here.

list = (Cliente, Fabricante, Veiculo, Tabela, Mensalista, Rotativo, FormaPagamento)

admin.site.register(list)

"""admin.site.register(Cliente)
admin.site.register(Fabricante)
admin.site.register(Veiculo)
admin.site.register(Tabela)
admin.site.register(Mensalista)
admin.site.register(Rotativo)"""
