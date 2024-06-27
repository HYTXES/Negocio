from django.contrib import admin
from.models import Comida


class ComidaAdmin(admin.ModelAdmin):
    list_display = ('name', 'descripcion', 'precio','stock')

admin.site.register(Comida,ComidaAdmin)
