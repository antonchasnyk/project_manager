from django.shortcuts import render, get_object_or_404
from .models import Bom, Pcb

# Create your views here.


def index(request):
    queryset = Pcb.objects.all()
    return render(request, 'index.html', context={'pcbs': queryset})


def pcb_detail(request, id):
    pcb = get_object_or_404(Pcb, pk=id)
    return render(request, 'pcb_detail.html', context={'pcb':pcb})


def bom_detail(request, id):
    bom = get_object_or_404(Bom, pk=id)
    components = bom.bomcomponent_set.all()
    counted_components = {}
    for comp in components:
        if comp.component_id in counted_components:
            counted_components[comp.component_id]['count'] += 1
            counted_components[comp.component_id]['annotation']+= ', {}'.format(comp.annotation)
        else:
            counted_components[comp.component_id] = {'count': 1, 'el': comp.component,
                                                     'annotation':str(comp.annotation)}

    context = {'bom': str(bom), 'components': counted_components.values()}
    return render(request, 'bom_detail.html', context=context)