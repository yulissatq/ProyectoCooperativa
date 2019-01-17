from django.urls import path 

from . import views

urlpatterns = [
    path('loginPage/', views.loginPage, name ='autenticar'),
    path('logoutPage/', views.logoutPage, name ='logoutPage')
]
