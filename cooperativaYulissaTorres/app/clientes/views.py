from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import FormularioCliente, FormularioCuenta, FormularioMonto, FormularioTransaccion
from app.modelo.models import Cliente, Cuenta, Transaccion

from weasyprint import HTML, CSS
from django.template.loader import get_template, render_to_string


# Create your views here.

@login_required
def principal(request):
    return render(request, 'principal/principal.html')

@login_required
def clientes(request):
    listaClientes = Cliente.objects.all().filter(estado=True).order_by('apellidos')
    context = {
        'listaC': listaClientes,
    }
    return render(request, 'clientes/clientes.html', context)
    

@login_required
def cuentas(request):

    listaCuentas = Cliente.objects.all().filter(estado=True).values('cedula', 'nombres', 'apellidos', 'estado', 'cuenta__numero', 'cuenta__saldo', 'cuenta__tipoCuenta').order_by('apellidos')
    return render(request, 'cuentas/cuentas.html', locals())
    

@login_required
def gestion_clientes(request):
    usuario = request.user
    if  usuario.has_perm('modelo.add_cliente'):
        listaClientesGestion = Cliente.objects.all().order_by('apellidos')
        context = {
            'lista': listaClientesGestion,
        }
        return render(request, 'clientes/gestion_clientes.html', context)
    else: 
        return render(request, 'login/acceso_prohibido.html')

@login_required
def buscar_gestion_cliente(request):
    usuario = request.user
    if  usuario.has_perm('modelo.add_cliente'):
        cedula = request.GET['cedula']
        listaClientesGestion = Cliente.objects.all().filter(cedula=cedula).order_by('apellidos')
        context = {
            'lista': listaClientesGestion,
        }
        return render(request, 'clientes/gestion_clientes.html', context)
    else: 
        return render(request, 'login/acceso_prohibido.html')

@login_required
def transacciones(request):
        listaCuentasTransac = Cliente.objects.all().filter(estado=True).values('cedula', 'nombres', 'apellidos', 'estado', 'correo', 'cuenta__numero', 'cuenta__saldo', 'cuenta__tipoCuenta').order_by('apellidos')
        return render(request, 'transacciones/transacciones.html', locals())

    
@login_required
def buscar_transacciones(request):
        cedula = request.GET['cedula']
        listaCuentasTransac = Cliente.objects.all().filter(cedula=cedula).values('cedula', 'nombres', 'apellidos', 'estado', 'correo', 'cuenta__numero', 'cuenta__saldo', 'cuenta__tipoCuenta').order_by('apellidos')
        return render(request, 'transacciones/transacciones.html', locals())

   
@login_required
def crear_cliente(request): 
    usuario = request.user
    if  usuario.has_perm('modelo.add_cliente'):
        formulario = FormularioCliente(request.POST)
        formularioCuenta = FormularioCuenta(request.POST)
        titulo = 'Creacion de Datos'
        if request.method == 'POST':
            if formulario.is_valid() and formularioCuenta.is_valid():
                cliente = Cliente()
                datos = formulario.cleaned_data
                cliente.cedula = datos.get('cedula')
                cliente.nombres = datos.get('nombres')
                cliente.apellidos = datos.get('apellidos')
                cliente.genero = datos.get('genero')
                cliente.estadoCivil =datos.get('estadoCivil')
                cliente.fechaNacimiento = datos.get('fechaNacimiento') 
                cliente.correo = datos.get('correo')
                cliente.telefono = datos.get('telefono')
                cliente.celular = datos.get('celular')
                cliente.direccion = datos.get('direccion')
                cliente.save()

                cuenta = Cuenta()
                datosCuenta = formularioCuenta.cleaned_data
                cuenta.numero = datosCuenta.get('numero')
                cuenta.saldo = datosCuenta.get('saldo')
                cuenta.tipoCuenta = datosCuenta.get('tipoCuenta')
                cuenta.cliente = cliente
                cuenta.save()
                return redirect(gestion_clientes)
        context={
            'f': formulario,
            'fc': formularioCuenta,
            'mensaje': 'Bienvenidos', 
        }
        return render(request, 'clientes/crear_cliente.html', context)
    else: 
        return render(request, 'login/acceso_prohibido.html')

@login_required
def modificar_cliente(request,pk):
    cliente = Cliente.objects.get(cedula = pk)
    formulario = FormularioCliente(request.POST)
    if request.method == 'POST':
        formulario = FormularioCliente(request.POST)
        formulario.is_valid()
        datos = formulario.cleaned_data
        cliente.nombres = datos.get('nombres')
        cliente.apellidos = datos.get('apellidos')
        cliente.genero = datos.get('genero')
        cliente.estadoCivil =datos.get('estadoCivil')
        cliente.fechaNacimiento = datos.get('fechaNacimiento') 
        cliente.telefono = datos.get('telefono')
        cliente.celular = datos.get('celular')
        cliente.direccion = datos.get('direccion')
        cliente.save()
        return redirect(gestion_clientes)
    else:
        formulario = FormularioCliente(instance = cliente)
    context={
        'formulario': formulario,

    }
    return render(request, 'clientes/modificar_cliente.html', context)

@login_required
def inactivar_cliente(request,pk):
    cliente = Cliente.objects.get(cedula = pk)
    cliente.estado = False
    cliente.save()
    return redirect(gestion_clientes)

@login_required
def activar_cliente(request,pk):
    cliente = Cliente.objects.get(cedula = pk)
    cliente.estado = True
    cliente.save()
    return redirect(gestion_clientes)
      
@login_required
def depositar_retirar_transaccion(request, cedula, numero):
    formMonto = FormularioMonto(request.POST)
    formTransaccion =FormularioTransaccion(request.POST)
    cliente = Cliente.objects.all().filter(cedula = cedula)
    cuenta = Cuenta.objects.all().filter(numero = numero)
    if request.method == 'POST':
        if formMonto.is_valid() and formTransaccion.is_valid():
            datosMonto = formMonto.cleaned_data
            datosTransaccion = formTransaccion.cleaned_data
            transaccion = Transaccion()
            monto = float(datosTransaccion.get('valor'))
            dep = str(Cuenta.objects.get(numero = numero))
            dep = dep.split(';')
            saldoActual = float(dep[0])
            transaccion.tipo = datosTransaccion.get('tipo')
            transaccion.valor= datosTransaccion.get('valor')
            transaccion.descripcion = datosTransaccion.get('descripcion')
            transaccion.responsable = datosTransaccion.get('responsable')
            transaccion.cuenta = Cuenta.objects.get(cuenta_id = int(dep[1]))
            if datosTransaccion.get('tipo') == 'Deposito':
                transaccion.save()
                for cuen in cuenta:
                    cuen.saldo = round(saldoActual + monto, 3)
                    cuen.save()
                return render(request, 'transacciones/mensaje_transaccion.html', locals())
            if datosTransaccion.get('tipo') == 'Retiro':
                transaccion.save()
                for cuen in cuenta:
                    cuen.saldo = round(saldoActual - monto, 3)
                    cuen.save()
                return render(request, 'transacciones/mensaje_transaccion.html', locals())
    else:
        return render(request,'transacciones/depositar_retirar_transaccion.html', locals())

@login_required
def confirmar_contrasena(request):
    confirmar = False
    contrasena = request.GET['contrasena']
    if request.user.check_password(contrasena):
        confirmar=True
    return HttpResponse(confirmar)

@login_required
def obtener_user(request):
    user = request.user.username
    return HttpResponse(user)

@login_required
def transferencias(request):
    return render(request, 'transferencias/transferencias.html')


@login_required
def buscar_transferenciaOrigen(request):
        confirmar = False
        numero = request.GET['numero']
        lista= Cliente.objects.all().filter(cuenta__numero=numero).values('cedula','nombres','apellidos','correo','cuenta__numero',
        'cuenta__saldo','cuenta__tipoCuenta').order_by('apellidos')
        listaCuenta= Cuenta.objects.all().filter(numero=numero).values('numero',
        'saldo','tipoCuenta')
        data = ''
        for i in lista.values():
               data =i['cedula']+";"+i['nombres']+";"+i['apellidos']+";"+i['correo']+";"
        
        for i in listaCuenta.values():
                data += i['numero']+";"+str(i['saldo'])+";"+i['tipoCuenta']
        
        return HttpResponse(data)          

@login_required
def transferencia(request):
        numero1 = request.GET['numero1']
        cedula1= request.GET['cedula1']
        numero2 = request.GET['numero2']
        cedula2 = request.GET['cedula2']
        valor = request.GET['monto']
        descripcion = request.GET['descripcion']
        responsable = request.GET['responsable']

        cliente1=Cliente.objects.all().filter(cedula = cedula1)
        cuenta1 = Cuenta.objects.all().filter(numero = numero1)

        cliente2=Cliente.objects.all().filter(cedula = cedula2)
        cuenta2 = Cuenta.objects.all().filter(numero = numero2)

        titulo ="Transaccion estado"
        subtitulo ="Mensaje"

        if cliente1 and cuenta1 and cliente2 and cuenta2:
                transaccion = Transaccion()

                auxCuenta1=str(Cuenta.objects.get(numero = numero1))
                auxCuenta2=str(Cuenta.objects.get(numero = numero2))

                auxCuenta1 =  auxCuenta1.split(';')
                auxCuenta2 =  auxCuenta2.split(';')

                saldoActual1 = float(auxCuenta1[0])
                saldoActual2 = float(auxCuenta2[0])

                transaccion.tipo= 'Transferencia'
                transaccion.valor = round(float(valor),3)
                transaccion.descripcion = descripcion
                transaccion.responsable = responsable
                transaccion.cuenta = Cuenta.objects.get(cuenta_id=int(auxCuenta1[1]))

                deposito = float(valor)
               
                for cu in cuenta1:
                        cu.saldo =round(saldoActual1-deposito,3)
                        cu.save()
                
                transaccion.save()

                for cu in cuenta2:
                        cu.saldo =round(saldoActual2+deposito,3)
                        cu.save()
                mensaje ='Transaccin realizada con éxito'
                valor = valor
                return render (request,'transferencias/mensaje_transferencia.html',locals())
        else:
                valor = valor
                mensaje ='ERROR AL REALIZAR TRANSACCION'
                return render (request,'transferencias/mensaje_transferencia.html',locals())


@login_required
def historial_transacciones(request):
        listaHistorial = Transaccion.objects.all().filter(Q(tipo='Retiro') | Q(tipo='Deposito')).values('tipo', 'valor', 'fecha', 'responsable', 'cuenta__numero', 'cuenta__tipoCuenta').order_by('fecha')
        return render(request, 'transacciones/historial_transacciones.html', locals())

@login_required
def historial_transferencias(request):
        listaHistorial = Transaccion.objects.all().filter(tipo = "Transferencia").values('tipo', 'valor', 'fecha', 'responsable', 'descripcion', 'cuenta__numero', 'cuenta__tipoCuenta').order_by('fecha')
        return render(request, 'transferencias/historial_transferencias.html', locals())

@login_required
def generar_comprobante(request):
    numero= request.GET['numero']
    cedula= request.GET['cedula']
    monto = request.GET['monto']
    user = request.user.username

    print("*---------------------------------------------------------------------------")
    print(numero)
    print(cedula)
    print(monto)
    print("*---------------------------------------------------------------------------")

    clientes = Cliente.objects.all().filter(cedula= cedula).values('nombres','apellidos')
    cuentas = Cuenta.objects.all().filter(numero = numero).values('tipoCuenta', 'saldo')
    
    template = render_to_string('./../template/comprobantes/comprobantes.html', locals())
    enviarComprobante = HttpResponse(content_type = 'application/pdf')

    pdf_comprobante = HTML(string = template).write_pdf()
    enviarComprobante = HttpResponse(pdf_comprobante, content_type = 'application/pdf')

    enviarComprobante['Content-Disposition'] = 'filename="comprobante.pdf"'

    return enviarComprobante  






      