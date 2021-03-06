# Generated by Django 2.1.4 on 2018-12-28 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0005_auto_20181227_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='tipoCuenta',
            field=models.CharField(choices=[('Corriente', 'Corriente'), ('Ahorros', 'Ahorro'), ('Basica', 'Básica'), ('Nomina', 'Nómina'), ('Valores', 'Valores'), ('Juvenil', 'Juvenil'), ('Programado', 'Ahorro Programado'), ('Euros', 'Ahorro en Euros')], max_length=30),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='tipo',
            field=models.CharField(choices=[('Retiro', 'Retiro'), ('Deposito', 'Depósito'), ('Transferencia', 'Transferencia'), ('Prestamo', 'Pago de Prestamo'), ('Nomina', 'Pagos de Nómina'), ('Pensiones', 'Pagos de Pensiones'), ('Dividendos', 'Dividendos'), ('ReembolsoGastos', 'Reembolso de Gastos'), ('PagoProveedores', 'Reembolso de Gastos'), ('Transferencia', 'Traslado de efectivo entre entidades bancarias'), ('Seguros', 'Pago de Seguros'), ('Iess', 'Pago del IESS'), ('Hipotecas', 'Pago de Hipotecas'), ('ServiciosBasico', 'Pago de Servicios Básicos'), ('TvCable', 'Cuentas de televisión por cable'), ('Celular', 'Cuentas de celular'), ('Online', 'Compras por Internet'), ('Administracion', 'Servicio de Administración'), ('Futuros', 'Pagos Futuros')], max_length=30),
        ),
    ]
