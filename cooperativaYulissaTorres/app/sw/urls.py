from django.urls import path
from . import views

urlpatterns = [
path('listaClientes', views.ListaClientes.as_view()),
path('listaClienteCedula/', views.ListaClienteCedula.as_view()),
path('listaCuentas', views.ListaCuentas.as_view()),
path('listaCuentaCedula/', views.ListaCuentaNumero.as_view()),
path('listaTransacciones', views.ListaTransacciones.as_view()),
path('listaTransaccionId/', views.ListaTransaccionId.as_view()),
]