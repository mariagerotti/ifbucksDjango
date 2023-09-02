# Generated by Django 4.2.4 on 2023-09-02 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ifbucks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(null=True, upload_to='media')),
            ],
            options={
                'verbose_name': 'Imagem',
                'verbose_name_plural': 'Imagens',
            },
        ),
        migrations.AddField(
            model_name='pedido',
            name='foto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ifbucks.imagem'),
        ),
        migrations.AddField(
            model_name='produto',
            name='foto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ifbucks.imagem'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='imagem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ifbucks.imagem'),
        ),
    ]
