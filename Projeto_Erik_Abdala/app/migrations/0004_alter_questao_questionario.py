# Generated by Django 4.2.7 on 2023-11-13 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_questionario_questao_questao_questionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questao',
            name='questionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.questionario'),
        ),
    ]
