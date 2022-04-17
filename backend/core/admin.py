from django.contrib import admin
from .models.models_clientes import Dossie
from .models.models_params import ParamsUser


class DossieAdmin(admin.ModelAdmin):
    list_display = ("name", "state", "email", "created_at", "updated_at")


class ParamsUserAdmin(admin.ModelAdmin):
    list_display = ("project", "description", "dossie")


admin.site.register(Dossie, DossieAdmin)
admin.site.register(ParamsUser, ParamsUserAdmin)
