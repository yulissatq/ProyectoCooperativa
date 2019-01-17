from django.contrib import admin

# Register your models here.
from .models import Cliente
from .models import Banco
from .models import Cuenta
from .models import Transaccion

class AdminCliente(admin.ModelAdmin):

    list_display = ["cedula", "nombres", "apellidos", "genero", "estadoCivil", "fechaNacimiento", "correo", "telefono", "celular", "direccion"]
    list_editable = ["apellidos", "nombres", "genero"]
    list_filter = ["genero", "direccion", "fechaNacimiento", "estadoCivil"]
    search_fields = ["cedula", "nombres", "apellidos"]

    class Meta:
        model = Cliente

admin.site.register(Cliente, AdminCliente)

class AdminBanco(admin.ModelAdmin):
    list_display = ["nombreB", "direccionB", "telefonoB", "correoB"]
    list_editable = ["direccionB", "telefonoB", "correoB"]
    list_filter = ["direccionB"]
    search_fields = ["nombreB", "correoB"]

    class Meta:
        model = Banco

admin.site.register(Banco, AdminBanco)

class AdminCuenta(admin.ModelAdmin):

    list_display = ["numero", "estadoC", "fechaApertura", "saldo", "tipoCuenta", "cliente"]
    list_filter = ["fechaApertura", "estadoC", "tipoCuenta"]
    search_fields = ["numero", "cliente"]

    class Meta:
        model = Cuenta

admin.site.register(Cuenta, AdminCuenta)

class AdminTransaccion(admin.ModelAdmin):

    list_display = ["fecha", "tipo", "valor", "descripcion", "responsable", "cuenta"]
    list_filter = ["tipo", "responsable"]
    search_fields = ["cuenta", "descripcion"]

    class Meta:
        model = Transaccion

admin.site.register(Transaccion, AdminTransaccion)
