from django.shortcuts import render, get_object_or_404
from .models import Resistor, Capacitor, Transistor, Component
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def get_boms(id):
    el = get_object_or_404(Component, pk=id)
    boms = el.bom_set.all().order_by('id').distinct('id')
    cboms = []
    for bom in boms:
        count = bom.components.filter(pk=el.id).count()
        cboms.append({'name': str(bom), 'bom': bom, 'count': count})
    return cboms


def components_detail(request, id):
    el = get_object_or_404(Component, pk=id)
    boms = get_boms(el.id)
    context = {'el': el, 'boms':boms}
    return render(request, 'component.html', context=context)


def components(request):
    return render(request, 'components.html')


def resistors(request):
    res = Resistor.objects.all()
    return render(request, 'resistors.html', context={'resistors':res})


def resistor_detail(request, id):
    res = get_object_or_404(Resistor, pk=id)
    boms = get_boms(res.id)
    context = {'el': res, 'boms': boms}
    return render(request, 'resistor_detail.html', context=context)


def capacitors(request):
    cap = Capacitor.objects.all()
    return render(request, 'capacitors.html', context={'capacitors':cap})


def capacitor_detail(request, id):
    cap = get_object_or_404(Capacitor, pk=id)
    boms = get_boms(cap.id)
    context = {'el': cap, 'boms': boms}
    return render(request, 'capacitor_detail.html', context=context)


def transistors(request):
    trans = Transistor.objects.all()
    return render(request, 'transistors.html', context={'transistros':trans})


def transistor_detail(request, id):
    trans = get_object_or_404(Transistor, pk=id)
    boms = get_boms(trans.id)
    context = {'el': trans, 'boms': boms}
    return render(request, 'transistor_detail.html', context=context)