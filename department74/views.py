from django.shortcuts import render, render_to_response
from django.utils import timezone
from .models import Comp, CompItems, Components
from .forms import ComponentsForm, PartForm
from django.shortcuts import redirect


def ind(request):
    return render(request, 'department74/ind.html', {})


def arrival(request):
    return render(request, 'department74/arrival.html', {})


def comp(request):
    if request.method == 'POST':
        form = PartForm(request.POST)
        if 'select' in request.POST:
            select = request.POST['select']
            if select == '':
                return render(request, 'department74/comp.html', {'form': form})
            comps = Comp.objects.filter(part_id=select)
            comps_serial = [c.serial_number for c in comps]
            items = CompItems.objects.filter(comp__serial_number__in=comps_serial)
            return render(request, 'department74/comp.html', {'form': form, 'comps': comps, 'items': items})
    form = PartForm()
    return render(request, 'department74/comp.html', {'form': form})


def components_list(request):
    components = Components.objects.filter(date_of_arrival__lte=timezone.now()).order_by('date_of_arrival')
    errors = []
    notfound = ''
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Введите поисковый запрос!')
            render_to_response('department74/components_list.html', {'components': components})
        elif len(q) > 50:
            errors.append('Много символов!')
        else:
            names = Components.objects.filter(name__icontains=q)
            serials = Components.objects.filter(serial_number__icontains=q)
            types = Components.objects.filter(name_type__name_type__icontains=q)
            part_names = Components.objects.filter(part_name__part_name__icontains=q)
            matches = list(serials) + list(names) + list(types) + list(part_names)
            if not matches:
                notfound = 'Ничего не найдено'
            return render_to_response('department74/components_list.html', {
                'matches': matches,
                'query': q,
                'notfound': notfound})

    return render_to_response('department74/components_list.html', {'errors': errors, 'components': components})


def components_new(request):
    if request.method == "POST":
        form = ComponentsForm(request.POST)
        if form.is_valid():
            new_component = form.save()
            new_component.save()
            return redirect('/components/new/')
    else:
        form = ComponentsForm()
    return render(request, 'department74/components_new.html', context={'form': form})
