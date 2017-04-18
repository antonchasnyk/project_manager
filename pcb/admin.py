from django.contrib import admin
from.models import Pcb, Bom, Footprint, Resistor, BomComponent, \
    Capacitor, Transistor

# Register your models here.


@admin.register(Pcb)
class PcbAdmin(admin.ModelAdmin):
    pass


@admin.register(Footprint)
class FootprintAdmin(admin.ModelAdmin):
    pass


class ComponentInline(admin.TabularInline):
    model = BomComponent


@admin.register(Resistor)
class ResistorAdmin(admin.ModelAdmin):
    pass


@admin.register(Capacitor)
class CapacitorAdmin(admin.ModelAdmin):
    pass


@admin.register(Transistor)
class TransistorAdmin(admin.ModelAdmin):
    pass

@admin.register(Bom)
class BomAdmin(admin.ModelAdmin):
    inlines = ComponentInline,