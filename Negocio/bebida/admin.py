from django.contrib import admin
from.models import Bebida


class BebidaAdmin(admin.ModelAdmin):
    list_display = ('name', 'descripcion', 'precio','stock')

admin.site.register(Bebida,BebidaAdmin)
