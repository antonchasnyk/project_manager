from django.shortcuts import render, get_object_or_404
from .models import Bom, Pcb, Resistor, Capacitor, Transistor

# Create your views here.


def index(request):
    queryset = Pcb.objects.all()
    context = {'pcbs': queryset}
    return render(request, 'index.html', context=context)


def bom_detail(request, id):
    bom = get_object_or_404(Bom, pk=id)
    components = bom.bomcomponent_set.all()
    counted_components = {}
    for comp in components:
        if comp.component_id in counted_components:
            counted_components[comp.component_id]['count'] += 1
            counted_components[comp.component_id]['annotation'].append(comp.annotation)
        else:
            counted_components[comp.component_id] = {'count': 1, 'name': comp.component.name,
                                                     'annotation':[comp.annotation]}
    context = {'bom': str(bom), 'components': counted_components.values()}
    return render(request, 'bom_detail.html', context=context)


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