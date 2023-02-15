from django.contrib import admin

from cadastro.models import Cidade, Estado, Pais

# Register your models here.


class EstadoInline(admin.TabularInline):

    model = Estado


class PaisAdmin(admin.ModelAdmin):

    fields = ('nome',)
    inlines = [
        EstadoInline
    ]


admin.site.register(Pais, PaisAdmin)
admin.site.register(Estado)
admin.site.register(Cidade)
