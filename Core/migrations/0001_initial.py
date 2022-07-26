# Generated by Django 4.0.3 on 2022-05-19 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('endereco', models.CharField(blank=True, max_length=75, null=True, verbose_name='Endereção')),
                ('complemento', models.CharField(blank=True, max_length=50, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bairro')),
                ('cidade', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cidade')),
                ('cep', models.CharField(blank=True, max_length=15, null=True, verbose_name='CEP')),
                ('email', models.CharField(max_length=50, verbose_name='E-mail')),
                ('telefone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos_clientes', verbose_name='Foto')),
            ],
            options={
                'verbose_name_plural': 'Cliente',
            },
        ),
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
            ],
            options={
                'verbose_name_plural': 'Fabricantes',
            },
        ),
        migrations.CreateModel(
            name='FormaPagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30, verbose_name='Forma de Pagamento')),
            ],
            options={
                'verbose_name_plural': 'Forma Pagamentos',
            },
        ),
        migrations.CreateModel(
            name='Tabela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('descricao_tab', models.CharField(max_length=35, verbose_name='Descrição')),
            ],
            options={
                'verbose_name_plural': 'Tabelas',
            },
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=25, verbose_name='Modelo')),
                ('placa', models.CharField(max_length=10, verbose_name='Placa')),
                ('ano', models.IntegerField(blank=True, default=2022, null=True, verbose_name='Ano')),
                ('cor', models.CharField(blank=True, max_length=15, null=True, verbose_name='Cor')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos_veiculos', verbose_name='Foto')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.cliente', verbose_name='Cliente')),
                ('id_fabricante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.fabricante', verbose_name='Fabricante')),
            ],
            options={
                'verbose_name_plural': 'Veiculo',
            },
        ),
        migrations.CreateModel(
            name='Rotativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrada', models.DateTimeField(verbose_name='Data de Entrada')),
                ('data_saida', models.DateTimeField(blank=True, null=True, verbose_name='Data da Saída')),
                ('pago', models.BooleanField(blank=True, default=False, null=True, verbose_name='Status Pagamento')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total')),
                ('id_tabela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.tabela', verbose_name='Preço')),
                ('id_veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.veiculo', verbose_name='Veiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Mensalista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_vencimento', models.IntegerField(default=5, verbose_name='Dia do vencimento')),
                ('em_pendencia', models.BooleanField(blank=True, default=False, null=True, verbose_name='Devedor')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.cliente', verbose_name='Cliente')),
                ('id_tabela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.tabela', verbose_name='Tarifa')),
            ],
            options={
                'verbose_name_plural': 'Mensalistas',
            },
        ),
    ]
