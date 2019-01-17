from django import forms
from app.modelo.models import Cliente, Cuenta, Transaccion


class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["cedula", "nombres", "apellidos", "genero", "estadoCivil", "fechaNacimiento", "correo", "telefono", "celular", "direccion"]
        widgets={
            'cedula' : forms.TextInput(attrs = {'placeholder':'Ingrese Cédula del Cliente'}),
            'nombres' : forms.TextInput(attrs = {'placeholder':'Ingrese Nombres del Cliente'}),
            'apellidos' : forms.TextInput(attrs = {'placeholder':'Ingrese Apellidos del Cliente'}),
            'fechaNacimiento': forms.DateInput(format = '%Y-%m-%d', attrs={'type':'date'}),
            'correo' : forms.TextInput(attrs = {'placeholder':'Ingrese Email del Cliente'}),
            'telefono' : forms.TextInput(attrs = {'placeholder':'Ingrese Teléfono del Cliente'}),
            'celular' : forms.TextInput(attrs = {'placeholder':'Ingrese Celular del Cliente'}),
            'direccion' : forms.TextInput(attrs = {'placeholder':'Ingrese Dirección del Cliente'}),
        }

class FormularioCuenta(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ["numero", "saldo", "tipoCuenta"]
        widgets= {
            'numero' : forms.TextInput(attrs = {'placeholder':'Ingrese Número de Cuenta del Cliente'}),
        }

class FormularioMonto(forms.Form):
    password = forms.CharField(widget = forms.PasswordInput(attrs={'type':'password', 'name':'pwd', 'id':'user_pass', 'class':'input', 'placeholder':'Ingrese Contraseña de Confirmación', 'value':'', 'size':'20', 'required': 'true' }))

class FormularioTransaccion(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ["tipo", "valor", "descripcion", "responsable"]
        widgets={
            'descripcion': forms.TextInput(attrs = {}),
            
        }
        
#class FormularioBanco(forms.ModelForm):
    #class Meta:
        #model = Banco
        #fields = ["nombreB", "direccionB", "telefonoB", "correoB"]
