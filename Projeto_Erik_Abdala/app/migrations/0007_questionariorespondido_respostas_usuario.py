# Generated by Django 4.2.7 on 2023-11-21 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_questao_alternativa_submetida'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionariorespondido',
            name='respostas_usuario',
            field=models.TextField(blank=True, null=True),
        ),
    ]
