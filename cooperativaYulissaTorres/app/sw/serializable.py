from rest_framework import serializers
from app.modelo.models import Cliente, Cuenta, Transaccion

class ClienteSerializable(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["cedula", "nombres", "apellidos", "genero", "estadoCivil", "fechaNacimiento", "correo", "telefono", "celular", "direccion"]

class CuentaSerializable(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = ["numero", "saldo", "tipoCuenta", "estadoC", "fechaApertura"]

class TransaccionSerializable(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = ["transaccion_id","tipo", "valor", "descripcion", "responsable", "fecha"]