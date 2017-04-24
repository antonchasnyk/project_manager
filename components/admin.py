from django import forms
from django.contrib import admin
from .models import Resistor, Capacitor, Transistor, Footprint
from django.utils.translation import ugettext as _
from .validators import res_validator, cap_validator

# Register your models here.


@admin.register(Footprint)
class FootprintAdmin(admin.ModelAdmin):
    pass


class ResAdminForm(forms.ModelForm):
    # custom field not backed by database
    obf_value = forms.CharField(label=_('Номинал'))

    class Meta:
        model = Resistor
        fields = '__all__'
        exclude = ('value',)

    def clean_obf_value(self):
        data = self.cleaned_data['obf_value']
        db = res_validator(data)
        return db

    def __init__(self, *args, **kwargs):
        # only change attributes if an instance is passed
        instance = kwargs.get('instance')
        if instance:
            self.base_fields['obf_value'].initial = instance.get_value()
        forms.ModelForm.__init__(self, *args, **kwargs)

@admin.register(Resistor)
class ResistorAdmin(admin.ModelAdmin):
    form = ResAdminForm

    def save_model(self, request, obj, form, change):
        obj.value = form.cleaned_data['obf_value']
        obj.save()


class CapAdminForm(forms.ModelForm):
    # custom field not backed by database
    obf_value = forms.CharField(label=_('Номинал'))

    class Meta:
        model = Capacitor
        fields = '__all__'
        exclude = ('value',)

    def clean_obf_value(self):
        data = self.cleaned_data['obf_value']
        db = cap_validator(data)
        return db

    def __init__(self, *args, **kwargs):
        # only change attributes if an instance is passed
        instance = kwargs.get('instance')
        if instance:
            self.base_fields['obf_value'].initial = instance.get_value()
        forms.ModelForm.__init__(self, *args, **kwargs)


@admin.register(Capacitor)
class CapacitorAdmin(admin.ModelAdmin):
    form = CapAdminForm

    def save_model(self, request, obj, form, change):
        obj.value = form.cleaned_data['obf_value']
        obj.save()


@admin.register(Transistor)
class TransistorAdmin(admin.ModelAdmin):
    pass