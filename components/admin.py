from django.contrib import admin
from .models import Resistor, Capacitor, Transistor, Footprint

# Register your models here.

@admin.register(Footprint)
class FootprintAdmin(admin.ModelAdmin):
    pass

@admin.register(Resistor)
class ResistorAdmin(admin.ModelAdmin):
    pass


@admin.register(Capacitor)
class CapacitorAdmin(admin.ModelAdmin):
    pass


@admin.register(Transistor)
class TransistorAdmin(admin.ModelAdmin):
    pass