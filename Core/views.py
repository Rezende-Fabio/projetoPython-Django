from urllib import request
from django.shortcuts import render, redirect
from Core.formes import *
from Core.models import Cliente, Fabricante, Veiculo
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def home(request):
    if request.POST:
        valor = request.POST['i_nome']
    else: valor = ""
    contexto = {"valor": valor}
    return render(request, "Core/index.html", contexto)


class Registrar(generic.CreateView):
    form_class = UserCreationForm
    succes_url = "/"
    template_name = "registration/register.html"


def cadastro_cliente(request):
    try:
        form = FormCliente(request.POST or None, request.FILES or None)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            form.save()
            messages.success(request, f"Cliente {nome} Cadastrado com Sucesso!!")
            return redirect("Lista_Clientes")
        else:
            contexto = {"form": form, "titulo": "Cadatro de Cliente", "strigBotao": "Cadastrar"}
            return render(request, "Core/cadastro.html", contexto)
    except Exception as mensagem_erro:
        contexto = {"msg_erro": mensagem_erro}
        return render(request, '500.html', contexto)

def lista_clientes(request):
    try:
        dados = Cliente.objects.all()
        contexto = {"dados": dados}
        if request.POST:
            if request.POST['pesquisa']:
                dados = Cliente.objects.filter(nome=request.POST['pesquisa'])
        contexto = {'dados': dados}
        return render(request, "Core/lista_clientes.html", contexto)
    except Exception as mensagem_erro:
        contexto = {"msg_erro": mensagem_erro}
        return render(request, '500.html', contexto)

def cadastro_veiculo(request):
    try:
        form = FormVeiculo(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect("url_principal")
        else:
            contexto = {"form": form, "titulo": "Cadatro de Veículo", "strigBotao": "Cadastrar"}

        return render(request, "Core/cadastro.html", contexto)
    except Exception as mensagem_erro:
        contexto = {"msg_erro": mensagem_erro}
        return render(request, '500.html', contexto)

def lista_veiculos(request):
    try:
        dados = Veiculo.objects.all()
        contexto = {"dados": dados}
        if request.POST:
            if request.POST['pesquisa']:
                dados = Veiculo.objects.filter(placa=request.POST['pesquisa'])
        contexto = {"dados": dados}
        return render(request, "Core/lista_veiculos.html", contexto)
    except Exception as mensagem_erro:
        contexto = {"msg_erro": mensagem_erro}
        return render(request, '500.html', contexto)

def cadastro_fabricante(request):
    try:
        form = FormFabricante(request.POST or None, request.FILES or None)

        if form.is_valid():
            form.save()
            return redirect("url_principal")

        else:
            contexto = {"form": form, "titulo": "Cadatro de Fabricantes", "strigBotao": "Cadastrar"}
        
        return render(request, "Core/cadastro.html", contexto)
    except Exception as mensagem_erro:
        contexto = {"msg_erro": mensagem_erro}
        return render(request, '500.html', contexto)

def lista_de_fabricantes(request):
    try:
        dados = Fabricante.objects.all()
        contexto = {"dados": dados}
        if request.POST:
            if request.POST['pesquisa']:
                dados = Fabricante.objects.filter(descricao=request.POST['pesquisa'])
        contexto = {"dados": dados}
        return render(request, "Core/lista_fabricantes.html", contexto)
    except Exception as mensagem_erro:
        contexto = {"msg_erro": mensagem_erro}
        return render(request, '500.html', contexto)

def alterar_cliente(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
        form = FormCliente(request.POST or None, request.FILES or None, instance=cliente)

        if form.is_valid():
            nome = form.cleaned_data["nome"]
            form.save()
            messages.success(request, f"Dados do Cliente {nome} atulizados com Sucesso!")
            return redirect("Lista_Clientes")

        contexto = {'form': form, "titulo": "Atualizar Cliente", "strigBotao": "Salvar"}
        return render(request, "Core/cadastro.html", contexto)
    except Exception as mensagem_erro:
        contexto = {"msg_erro": mensagem_erro}
        return render(request, '500.html', contexto)

def exclui_cliente(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
        if request.POST:
            cliente.delete()
            contexto = {"verifica": False, "objeto": cliente.nome}
            return render(request, "Core/lista_clientes.html", contexto)
        contexto = {"url": "/lista_clientes/", "objeto": cliente.nome}
        return render(request, "Core/confrima_exclusao.html", contexto)
    except Exception as mensagem_erro:
        contexto = {"msg_erro": mensagem_erro}
        return render(request, '500.html', contexto)

def alterar_veiculo(request, id):
    try:
        veiculo = Veiculo.objects.get(id=id)
        form = FormVeiculo(request.POST or None, request.FILES or None, instance=veiculo)

        if form.is_valid():
            form.save()
            contexto = {'objeto': veiculo.modelo, 'url': '/lista_veiculos/'}
            return render(request, "Core/mensagem_salvo.html", contexto)

        contexto = {'form': form, "titulo": "Atualizar Veiculo", "strigBotao": "Salvar"}
        return render(request, "Core/cadastro.html", contexto)
    except Exception as mensagem_erro:
        contexto = {"msg_erro": mensagem_erro}
        return render(request, '500.html', contexto)

def exclui_veiculo(request, id):
    try:
        veiculo = Veiculo.objects.get(id=id)
        if request.POST:
            veiculo.delete()
            contexto = {"objeto": veiculo.modelo, "url": "/lista_veiculos/"}
            return render(request, "Core/mensagem_exclusao.html", contexto)
        contexto = {"url": "/lista_veiculos/", "objeto": veiculo.modelo}
        return render(request, "Core/confrima_exclusao.html", contexto)
    except Exception as mensagem_erro:
        contexto = {"msg_erro": mensagem_erro}
        return render(request, '500.html', contexto)

def alterar_fabricante(request, id):
    try:
        fabricante = Fabricante.objects.get(id=id)
        form = FormFabricante(request.POST or None, request.FILES or None, instance=fabricante)

        if form.is_valid():
            form.save()
            contexto = {'objeto': fabricante.descricao, 'url': '/lista_de_fabricantes/'}
            return render(request, "Core/mensagem_salvo.html", contexto)

        contexto = {'form': form, "titulo": "Atualizar Fabricante", "strigBotao": "Salvar"}
        return render(request, "Core/cadastro.html", contexto)
    except Exception as mensagem_erro:
        contexto = {"msg_erro": mensagem_erro}
        return render(request, '500.html', contexto)

def exclui_fabricante(request, id):
    try:
        veiculo = Fabricante.objects.get(id=id)
        if request.POST:
            veiculo.delete()
            contexto = {"objeto": veiculo.descricao, "url": "/lista_de_fabricantes/"}
            return render(request, "Core/mensagem_exclusao.html", contexto)
        contexto = {"url": "/lista_de_fabricantes/", "objeto": veiculo.descricao}
        return render(request, "Core/confrima_exclusao.html", contexto)
    except Exception as mensagem_erro:
        contexto = {"msg_erro": mensagem_erro}
        return render(request, '500.html', contexto)

def cadastro_rotativo(request):
    try:
        form = FormRotativoCadastro(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("Lista Rotativos")
        contexto = {"form": form, "titulo":"Cadastro de Rotativo", "strigBotao": "Cadastrar", "calendario": True}
        return render(request, "Core/cadastro.html", contexto)
    except Exception as mensagem_erro:
        contexto = {"msg_erro": mensagem_erro}
        return render(request, '500.html', contexto)

def lista_de_rotativos(request):
    try:
        dados = Rotativo.objects.all()
        contexto = {"dados": dados}
        if request.POST:
            if request.POST['pesquisa']:
                dados = Rotativo.objects.filter(id_veiculo=int(request.POST['pesquisa']))
        contexto = {"dados": dados}
        return render(request, "Core/lista_rotativos.html", contexto)
    except Exception as mensagem_erro:
        contexto = {"msg_erro": mensagem_erro}
        return render(request, '500.html', contexto)

def alterar_rotativo(request, id):
    try:
        rotativo = Rotativo.objects.get(id=id)
        form = FormRotativo(request.POST or None, instance=rotativo)

        if form.is_valid():
            rotativo.calculaTotal()
            form.save()
            contexto = {'objeto': rotativo.id_veiculo, 'url': '/lista_de_rotativos/'}
            return render(request, "Core/mensagem_salvo.html", contexto)

        contexto = {'form': form, "titulo": "Atualizar Rotativo", "strigBotao": "Salvar", "calendario": True}
        return render(request, "Core/cadastro.html", contexto)
    except Exception as mensagem_erro:
        contexto = {"msg_erro": mensagem_erro}
        return render(request, '500.html', contexto)


def exclui_rotativo(request, id):
    try:
        rotativo = Rotativo.objects.get(id=id)
        if request.POST:
            rotativo.delete()
            contexto = {"objeto": rotativo.id_veiculo, "url": "/lista_de_rotativos/"}
            return render(request, "Core/mensagem_exclusao.html", contexto)
        contexto = {"url": "/lista_de_rotativos/", "objeto": rotativo.id_veiculo}
        return render(request, "Core/confrima_exclusao.html", contexto)
    except Exception as mensagem_erro:
        contexto = {"msg_erro": mensagem_erro}
        return render(request, '500.html', contexto)


def lista_tabela(request):
    try:
        dados = Tabela.objects.all()
        contexto = {"dados":dados}
        return render(request, 'Core/tabela_de_precos.html', contexto)
    except Exception as mensagem_erro:
        contexto = {"msg_erro": mensagem_erro}
        return render(request, '500.html', contexto)


def cadastro_mensalista(request):
    try:
        form = FormMensalista(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("Lista Mensalistas")
        contexto = {"form": form, "titulo":"Cadastro de Mensalista", "strigBotao": "Cadastra"}
        return render(request, "Core/cadastro.html", contexto)
    except Exception as mensagem_erro:
        contexto = {"msg_erro": mensagem_erro}
        return render(request, '500.html', contexto)


def lista_mensalista(request):
    try:
        dados = Mensalista.objects.all()
        contexto = {"dados": dados}
        if request.POST:
            if request.POST['pesquisa']:
                dados = Mensalista.objects.filter(id_cliente=int(request.POST['pesquisa']))
        contexto = {"dados": dados}
        return render(request, "Core/lista_mensalista.html", contexto)
    except Exception as mensagem_erro:
        contexto = {"msg_erro": mensagem_erro}
        return render(request, '500.html', contexto)


def alterar_mensalista(request, id):
    try:
        mensalista = Mensalista.objects.get(id=id)
        form = FormMensalista(request.POST or None, instance=mensalista)

        if form.is_valid():
            form.save()
            contexto = {"objeto": mensalista.id_cliente, "url": "/lista_mensalistas/"}
            return render(request, "Core/mensagem_salvo.html", contexto)
        
        contexto = {"form": form, "titulo": "Atualizar Mensalistas", "strigBotao": "Salvar"}
        return render(request, "Core/cadastro.html", contexto)
    except Exception as mensagem_erro:
        contexto = {"msg_erro": mensagem_erro}
        return render(request, '500.html', contexto)

        
