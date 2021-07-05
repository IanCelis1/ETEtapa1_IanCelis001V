from django import forms 
from django.forms import ModelForm, widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Proveedor, Pais


class proveedorForm(ModelForm): 

    class Meta: 
        model = Proveedor 
        fields = ['iproveedor','fotoproveedor','nombreproveedor','Telefonoproveedor','direccionproveedor','emailproveedor','contrasenaproveedor','monedapago','pais']

        labels={
            'iproveedor': 'Digite Id',
            'fotoproveedor': 'escoja producto', 
            'nombreproveedor': 'Digite Nombre del proveedor', 
            'Telefonoproveedor': 'Digite el telefono del proveedor',
            'direccionproveedor': 'Digite la su direccion',
            'emailproveedor': 'Digite su email',
            'contrasenaproveedor': 'Digite su contraseña',
            'monedapago': 'Indique medio de pago',
            'pais': 'seleccione id de su pais'
        }

        widgets={

            'iproveedor': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'iproveedor', 
                    'id': 'iproveedor'
                }
            ),
            'foto': forms.FileInput(
                attrs={
                    'class': 'from-control',
                    'placeholder': 'foto', 
                    'id': 'foto'
                }
            ),
            'nombreproveedor': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'nombreproveedor', 
                    'id': 'nombreproveedor'
                }
            ),
            'Telefonoproveedor': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Telefonoproveedor', 
                    'id': 'Telefonoproveedor'
                }
            ), 
            'direccionproveedor': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'direccionproveedor', 
                    'id': 'direccionproveedor'
                }
            ),
            'emailproveedor': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'emailproveedor', 
                    'id': 'emailproveedor'
                }
            ),
            'contrasenaproveedor': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'contrasenaproveedor', 
                    'id': 'contrasenaproveedor'
                }
            ),
            'Telefonoproveedor': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Telefonoproveedor', 
                    'id': 'Telefonoproveedor'
                }
            ),
            'monedapago': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'monedapago', 
                    'id': 'monedapago'
                }
            ),
            'pais': forms.Select(    
                attrs={
                    'class': 'form-control', 
                    'id':'pais'
                }
            )  
        }