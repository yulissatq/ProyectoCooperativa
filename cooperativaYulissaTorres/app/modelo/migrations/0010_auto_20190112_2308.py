# Generated by Django 2.1.4 on 2019-01-12 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0009_auto_20181231_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='tipo',
            field=models.CharField(choices=[('Retiro', 'Retiro'), ('Deposito', 'Depósito'), ('Transferencia', 'Transferencia'), ('Prestamo', 'Pago de Prestamo')], max_length=30),
        ),
    ]