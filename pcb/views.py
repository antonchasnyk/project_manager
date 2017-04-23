from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Bom, Pcb

# Create your views here.


def index(request):
    """ Render HTML list view of all PCBs with pagination"""
    # TODO add warehouse and processing fields
    pcb_list = Pcb.objects.all()
    paginator = Paginator(pcb_list, 10)
    page = request.GET.get('page')
    try:
        pcbs = paginator.page(page)
    except PageNotAnInteger:
        pcbs = paginator.page(1) # If page is not an integer, deliver first page.
    except EmptyPage:
        pcbs = paginator.page(paginator.num_pages) # If page is out of range (e.g. 9999), deliver last page of results.

    return render(request,
                  'index.html',
                  {'pcbs': pcbs})


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