from django.contrib import admin
from .models import Galaxy, System, Planet
from import_export.admin import ExportActionMixin


@admin.register(Galaxy)
class GalaxyAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['name', 'id']


@admin.register(System)
class SystemAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['name', 'id']


@admin.register(Planet)
class PlanetAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['name', 'id']