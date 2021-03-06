# Generated by Django 2.1.4 on 2018-12-31 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0008_auto_20181228_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='tipo',
            field=models.CharField(choices=[('Retiro', 'Retiro'), ('Deposito', 'Depósito'), ('Transferencia', 'Transferencia'), ('Prestamo', 'Pago de Prestamo'), ('Nomina', 'Pagos de Nómina'), ('Pensiones', 'Pagos de Pensiones'), ('Dividendos', 'Dividendos'), ('ReembolsoGastos', 'Reembolso de Gastos'), ('PagoProveedores', 'Reembolso de Gastos'), ('TransferenciaBancaria', 'Traslado de efectivo entre entidades bancarias'), ('Seguros', 'Pago de Seguros'), ('Iess', 'Pago del IESS'), ('Hipotecas', 'Pago de Hipotecas'), ('ServiciosBasico', 'Pago de Servicios Básicos'), ('TvCable', 'Cuentas de televisión por cable'), ('Celular', 'Cuentas de celular'), ('Online', 'Compras por Internet'), ('Administracion', 'Servicio de Administración'), ('Futuros', 'Pagos Futuros')], max_length=30),
        ),
    ]
