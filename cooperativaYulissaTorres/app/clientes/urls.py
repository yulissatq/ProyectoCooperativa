from django.urls import path

from . import views

urlpatterns =[
    path('', views.principal, name='principal'),
    path('clientes/', views.clientes, name ='clientes'),
    path('cuentas/', views.cuentas, name ='cuentas'),
    path('gestion/', views.gestion_clientes, name ='gestion'),
    path('busquedaGestion/', views.buscar_gestion_cliente, name ='buscarGestion'),
    path('transacciones/', views.transacciones, name ='transacciones'),
    path('busquedaTransaccion/', views.buscar_transacciones, name = 'buscarTransaccion'),
    path('crear/', views.crear_cliente, name="crear"),
    path(r'^modificar/(?P<pk>\d+)/$', views.modificar_cliente, name='modificar'),
    path(r'^inactivar/(?P<pk>\d+)/$', views.inactivar_cliente, name='inactivar'),
    path(r'^activar/(?P<pk>\d+)/$', views.activar_cliente, name='activar'),
    path(r'^transaccion/(?P<cedula>\d+)(?P<numero>\d+)/$', views.depositar_retirar_transaccion, name='transaccion'),
    path('obtenerUser/', views.obtener_user, name='obtenerUser'),
    path('confirmarContrasena/', views.confirmar_contrasena, name='confirmar'),
    path('transferencias/', views.transferencias, name='transferencias'),
    path('transferencia/', views.transferencia, name='transferencia'),
    path('busquedaTransferenciaOrigen/', views.buscar_transferenciaOrigen, name='buscarTranferenciaOrigen'),
    path('historiaTransacciones/', views.historial_transacciones, name ='historialTransacciones'),
    path('historiaTransferencias/', views.historial_transferencias, name ='historialTransferencias'),
    path('comprobante/', views.generar_comprobante, name ='generarComprobante'),
]