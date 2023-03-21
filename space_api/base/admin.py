from django.contrib import admin
from .models import Galaxy, Systems, Planets


admin.site.register(Galaxy)
admin.site.register(Systems)
admin.site.register(Planets)