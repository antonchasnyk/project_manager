from django.shortcuts import render, get_object_or_404
from .models import Resistor, Capacitor, Transistor

# Create your views here.

def components_detail(request, id, type):
    el = None
    if type == 'capacitor':
        el = get_object_or_404(Capacitor, pk=id)
    context = {'el': el}
    return render(request, 'component.html', context=context)


def components(request):
    transistors = Transistor.objects.all()
    resistors = Resistor.objects.all()
    capacitors = Capacitor.objects.all()
    context={'R':resistors, 'C':capacitors, 'VT':transistors}
    return render(request, 'components.html', context=context)