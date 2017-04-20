from django.shortcuts import render, get_object_or_404
from .models import Resistor, Capacitor, Transistor, Component

# Create your views here.


def components_detail(request, id):
    el = get_object_or_404(Component, pk=id)
    boms = el.bom_set.all().order_by('id').distinct('id')
    cboms = []
    for bom in boms:
        count = bom.components.filter(pk=el.id).count()
        cboms.append({'name':str(bom),'bom':bom, 'count':count})
    context = {'el': el, 'cboms':cboms}
    return render(request, 'component.html', context=context)


def components(request):
    transistors = Transistor.objects.all()
    resistors = Resistor.objects.all()
    capacitors = Capacitor.objects.all()
    context={'R':resistors, 'C':capacitors, 'VT':transistors}
    return render(request, 'components.html', context=context)