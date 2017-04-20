from django.contrib import admin
from .models import Pcb, Bom, BomComponent

# Register your models here.

class ComponentInline(admin.TabularInline):
    model = BomComponent

@admin.register(Pcb)
class PcbAdmin(admin.ModelAdmin):
    pass


@admin.register(Bom)
class BomAdmin(admin.ModelAdmin):
    inlines = ComponentInline,