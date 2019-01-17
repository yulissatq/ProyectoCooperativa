from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from app.modelo.models import Cliente, Cuenta , Transaccion
from .serializable import ClienteSerializable, CuentaSerializable, TransaccionSerializable

# Create your views here.

class ListaClientes(APIView):    
    def get(self, request):
        lista = Cliente.objects.all()
        objetoSerializable = ClienteSerializable(lista, many = True)
        return  Response(objetoSerializable.data)

class ListaClienteCedula(APIView):  
    def get(self, request):
        cedula= request.GET["cedula"]
        
        lista = Cliente.objects.filter(cedula=cedula)
        objetoSerializable = ClienteSerializable(lista, many = True)
        return  Response(objetoSerializable.data)

class ListaCuentas(APIView):    
    def get(self, request):
        lista = Cuenta.objects.all()
        objetoSerializable = CuentaSerializable(lista, many = True)
        return  Response(objetoSerializable.data)

class ListaCuentaNumero(APIView):  
    def get(self, request):
        numero= request.GET["numero"]
        
        lista = Cliente.objects.filter(numero=numero)
        objetoSerializable = ClienteSerializable(lista, many = True)
        return  Response(objetoSerializable.data)

class ListaTransacciones(APIView):    
    def get(self, request):
        lista = Transaccion.objects.all()
        objetoSerializable = TransaccionSerializable(lista, many = True)
        return  Response(objetoSerializable.data)

class ListaTransaccionId(APIView):  
    def get(self, request):
        transaccion_id= request.GET["transaccion_id"]
        
        lista = Transaccion.objects.filter(transaccion_id=transaccion_id)
        objetoSerializable = TransaccionSerializable(lista, many = True)
        return  Response(objetoSerializable.data)


