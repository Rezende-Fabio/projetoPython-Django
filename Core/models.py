from django.db import models
from math import ceil, floor, trunc

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    endereco = models.CharField(max_length=75, blank=True, null=True, verbose_name="Endereção")
    complemento = models.CharField(max_length=50, blank=True, null=True, verbose_name="Complemento")
    bairro = models.CharField(max_length=50, blank=True, null=True, verbose_name="Bairro")
    cidade = models.CharField(max_length=50, blank=True, null=True, verbose_name="Cidade")
    cep = models.CharField(max_length=15, blank=True, null=True, verbose_name="CEP")
    email = models.CharField(max_length=50, verbose_name="E-mail")
    telefone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone")
    foto = models.ImageField(upload_to="fotos_clientes", blank=True, null=True, verbose_name="Foto")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Cliente"


class Fabricante(models.Model):
    descricao = models.CharField(max_length=50, verbose_name="Descrição")

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Fabricantes"


class Veiculo(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    id_fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, verbose_name="Fabricante")
    modelo = models.CharField(max_length=25, verbose_name="Modelo")
    placa = models.CharField(max_length=10, verbose_name="Placa")
    ano = models.IntegerField(default=2022, blank=True, null=True, verbose_name="Ano")
    cor = models.CharField(max_length=15, blank=True, null=True, verbose_name="Cor")
    foto = models.ImageField(upload_to="fotos_veiculos", blank=True, null=True, verbose_name="Foto")

    def __str__(self):
        return f"{self.placa} {self.modelo}"

    class Meta:
        verbose_name_plural = "Veiculo"


class Tabela(models.Model):
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    descricao_tab = models.CharField(max_length=35, verbose_name="Descrição")

    def __str__(self):
        return f"{self.descricao_tab} - ({self.preco})"

    class Meta:
        verbose_name_plural = "Tabelas"


class FormaPagamento(models.Model):
    descricao = models.CharField(max_length=30, verbose_name="Forma de Pagamento")
    
    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name_plural = "Forma Pagamentos"


class Mensalista(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    id_tabela = models.ForeignKey(Tabela, on_delete=models.CASCADE, verbose_name="Tarifa")
    dia_vencimento = models.IntegerField(default=5, verbose_name="Dia do vencimento")
    em_pendencia = models.BooleanField(default=False, blank=True, null=True, verbose_name="Devedor")
    id_formaPagamento = models.ForeignKey(FormaPagamento, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Forma de Pagamento")
    total = models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2, verbose_name="Total")

    def __str__(self):
        return f"{self.id_cliente} - {self.id_tabela} - {self.id_formaPagamento}"
    
    class Meta:
        verbose_name_plural = "Mensalistas"
    
    def calculoDesconto(self):
        formaPagato = FormaPagamento.objects.get(id = self.id_forma_pagamento.pk)
        taxa = Tabela.objects.get(id = self.id_tabela.pk)
        if formaPagato.descricao == "DINHEIRO":
            taxa.preco = float(taxa.preco) * 0.95
        elif formaPagato.descricao == "PIX":
            taxa.preco = float(taxa.preco) * 0.93
        else: 
            total = total.valor
        
        self.total = total
        return total


class Rotativo(models.Model):
    id_veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, verbose_name="Veiculo")
    id_tabela = models.ForeignKey(Tabela, on_delete=models.CASCADE, verbose_name="Preço")
    data_entrada = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name="Data de Entrada")
    data_saida = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name="Data da Saída")
    pago = models.BooleanField(default=False, blank=True, null=True, verbose_name="Status Pagamento")
    total = models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2, verbose_name="Total")

    def __str__(self):
        return f"{self.id_veiculo} - {self.data_entrada}"

    def calculaTotal(self):
        if self.data_saida:
            horas = (self.data_saida - self.data_entrada).total_seconds()/3600
            #Precisa buscar o valor na tebala de Preços. Ps. esta em outra tabela
            obj = Tabela.objects.get(id = self.id_tabela.pk) 
            adicional = float(obj.preco) * 0.6 
            if horas <= 0.5: 
                taxa = float(obj.preco) / 2.0
            else:
                tolerancia = (horas) - trunc(horas)
                if tolerancia <= 0.25: 
                    taxa = float(obj.preco) + ((floor(horas - 1)) * adicional)
                else:
                    taxa = float(obj.preco) + ((ceil(horas - 1)) * adicional)

            self.total = taxa
            return True
        else: 
            return False