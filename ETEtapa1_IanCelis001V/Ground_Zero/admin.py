from django.contrib import admin
from  .models import Pais, Proveedor, Productos
# Register your models here.
admin.site.register(Pais)
admin.site.register(Proveedor)
admin.site.register(Productos)