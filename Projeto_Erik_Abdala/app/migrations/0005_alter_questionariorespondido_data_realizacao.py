# Generated by Django 4.2.7 on 2023-11-16 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_questao_questionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionariorespondido',
            name='data_realizacao',
            field=models.DateTimeField(),
        ),
    ]
