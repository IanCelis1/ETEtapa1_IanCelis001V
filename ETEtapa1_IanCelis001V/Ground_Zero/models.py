from django.db import models

# Create your models here.

#Modelo para usuario
class Pais(models.Model):
    idpais = models.IntegerField(primary_key=True, verbose_name='Id de pais')
    nombrepais = models.CharField(max_length=50, verbose_name='Nombre del país')
    def __int__(self):

        return self.idpais


class Proveedor(models.Model):
    iproveedor = models.IntegerField(primary_key=True, verbose_name='Id de proveedor')
    fotoproveedor = models.ImageField(upload_to='Proveedores', null=True)
    nombreproveedor = models.CharField(max_length=16, verbose_name='Nombre de proveedor')
    Telefonoproveedor = models.CharField(max_length=12,verbose_name='telefono de proveedor')
    direccionproveedor = models.CharField(max_length=100,verbose_name='telefono de proveedor')
    emailproveedor = models.CharField(max_length=100,verbose_name='telefono de proveedor')
    contrasenaproveedor = models.CharField(max_length=12,verbose_name='contraseña')
    monedapago = models.CharField(max_length=7,verbose_name='tipo de moneda de pago')
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    def __int__(self):

        return self.iproveedor


class Productos(models.Model):
    idproducto = models.IntegerField(primary_key=True, verbose_name='Id de producto')
    monproducto = models.CharField(max_length=100, verbose_name='Nombre de producto')
    valorproducto = models.CharField(max_length=100, verbose_name='valor producto')
    Proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    def __int__(self):

        return self.idproducto
 