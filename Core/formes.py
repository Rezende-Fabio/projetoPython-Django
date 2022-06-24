from pyexpat import model
from django.forms import ModelForm
from Core.models import *
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class FormFabricante(ModelForm):
    class Meta:
        model = Fabricante
        fields = "__all__"


class FormCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"


class FormVeiculo(ModelForm):
    class Meta:
        model = Veiculo
        fields = "__all__"


class FormRotativo(ModelForm):
    class Meta:
        model = Rotativo
        fields = "__all__"
        widgets = {'data_entrada': DateTimePickerInput(), 'data_saida':DateTimePickerInput()}


class FormRotativoCadastro(ModelForm):
    class Meta:
        model = Rotativo
        fields = ["data_entrada", "id_veiculo", "id_tabela"]
        widgets = {'data_entrada': DateTimePickerInput(), 'data_saida':DateTimePickerInput()}


class FormMensalista(ModelForm):
    class Meta:
        model = Mensalista
        fields = "__all__"
    
    
class FormTabela(ModelForm):
    class Meta:
        model = Tabela
        fields = "__all__"