# Generated by Django 2.1.4 on 2018-12-27 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0004_cliente_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estadoCivil',
            field=models.CharField(choices=[('Soltero(a)', 'Soltero(a)'), ('Casado(a)', 'Casado(a)'), ('Viudo(a)', 'Viudo(a)'), ('Divoriado(a)', 'Divorciado(a)')], max_length=15),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='genero',
            field=models.CharField(choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino')], max_length=15),
        ),
    ]
