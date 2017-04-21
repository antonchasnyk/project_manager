from django.contrib import admin
from .models import Pcb, Bom, BomComponent, Schematic

# Register your models here.


class ComponentInline(admin.TabularInline):
    model = BomComponent


class SchematicInline(admin.TabularInline): # TODO Make required
    model = Schematic


@admin.register(Pcb)
class PcbAdmin(admin.ModelAdmin):
    inlines = SchematicInline,


@admin.register(Bom)
class BomAdmin(admin.ModelAdmin):
    inlines = ComponentInline,