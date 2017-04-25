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
    """
        Form provide custom field to interact with value field
        Validator must convert input to mOhms or raise Validation Error
    """
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
        # provide a initial value in standard units
        instance = kwargs.get('instance')
        if instance:
            self.base_fields['obf_value'].initial = instance.get_value()
        forms.ModelForm.__init__(self, *args, **kwargs)


@admin.register(Resistor)
class ResistorAdmin(admin.ModelAdmin):
    """
        replace value by cleaned_obf_value before save
    """
    form = ResAdminForm

    def save_model(self, request, obj, form, change):
        obj.value = form.cleaned_data['obf_value']
        obj.save()


class CapAdminForm(forms.ModelForm):
    """
        Form provide custom field to interact with value field
        Validator must convert input to femtofarads or raise Validation Error
    """
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
        # provide a initial value in standard units
        instance = kwargs.get('instance')
        if instance:
            self.base_fields['obf_value'].initial = instance.get_value()
        forms.ModelForm.__init__(self, *args, **kwargs)


@admin.register(Capacitor)
class CapacitorAdmin(admin.ModelAdmin):
    """
        replace value by cleaned_obf_value before save
    """
    form = CapAdminForm

    def save_model(self, request, obj, form, change):
        obj.value = form.cleaned_data['obf_value']
        obj.save()


@admin.register(Transistor)
class TransistorAdmin(admin.ModelAdmin):
    pass