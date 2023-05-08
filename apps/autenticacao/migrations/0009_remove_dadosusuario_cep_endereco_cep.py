# Generated by Django 4.1.7 on 2023-05-08 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0008_dadosusuario_cep'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dadosusuario',
            name='cep',
        ),
        migrations.AddField(
            model_name='endereco',
            name='cep',
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
    ]