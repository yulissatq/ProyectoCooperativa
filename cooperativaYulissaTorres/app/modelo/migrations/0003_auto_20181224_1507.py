# Generated by Django 2.1.4 on 2018-12-24 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0002_auto_20181224_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estadoCivil',
            field=models.CharField(choices=[('soltero(a)', 'Soltero(a)'), ('casado(a)', 'Casado(a)'), ('viudo(a)', 'Viudo(a)'), ('divoriado(a)', 'Divorciado(a)')], max_length=15),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='genero',
            field=models.CharField(choices=[('femenino', 'Femenino'), ('masculino', 'Masculino')], max_length=15),
        ),
    ]
