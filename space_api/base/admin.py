from django.contrib import admin
from .models import Galaxy, System, Planet, Owner, Rocket


admin.site.register(Galaxy)
admin.site.register(System)
admin.site.register(Planet)
admin.site.register(Owner)
admin.site.register(Rocket)
