# Generated by Django 5.0 on 2023-12-08 14:25

import django.db.models.deletion
import ifbucks.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='Categoria', max_length=100)),
                ('descricao', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(unique=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Mesa',
                'verbose_name_plural': 'Mesas',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('cargo', models.CharField(choices=[('Cliente', 'Cliente'), ('Garçom', 'Garçom'), ('Cozinheiro', 'Cozinheiro'), ('Gerente', 'Gerente')], default='Cliente', max_length=255)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('nome', models.CharField(default='Usuário', max_length=255)),
                ('imagem', models.FileField(blank=True, null=True, upload_to=ifbucks.models.user_image_upload_to)),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('mesa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='carrinhos', to='ifbucks.mesa')),
            ],
            options={
                'verbose_name': 'Carrinho',
                'verbose_name_plural': 'Carrinhos',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nome', models.CharField(max_length=250)),
                ('descricao', models.CharField(max_length=255)),
                ('imagem', models.FileField(blank=True, upload_to=ifbucks.models.produto_image_upload_to)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='ifbucks.categoria')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_pedido', models.DateTimeField(auto_now_add=True)),
                ('quantidade', models.IntegerField(default=1)),
                ('entregue', models.BooleanField(default=False)),
                ('carrinho', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pedidos', to='ifbucks.carrinho')),
                ('produto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ifbucks.produto')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.AddField(
            model_name='carrinho',
            name='items_pedidos',
            field=models.ManyToManyField(through='ifbucks.Pedido', to='ifbucks.produto'),
        ),
        migrations.AddField(
            model_name='carrinho',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carrinhos', to='ifbucks.usuario'),
        ),
    ]
