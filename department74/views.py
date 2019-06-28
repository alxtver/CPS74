from django.shortcuts import render, render_to_response
from django.utils import timezone
from .models import *
from .forms import ComponentsForm
from django.shortcuts import redirect


def ind(request):
    return render(request, 'department74/ind.html', {})


def arrival(request):
    return render(request, 'department74/arrival.html', {})


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
            errors.append('Дохрена символов!')
        else:
            names = Components.objects.filter(name__icontains=q)
            serials = Components.objects.filter(serial_number__icontains=q)
            types = Components.objects.filter(name_type__name_type__icontains=q)
            matches = list(serials) + list(names) + list(types)
            if not matches:
                notfound = 'Ничего не найдено'
            return render_to_response('department74/components_list.html', {'matches': matches, 'query': q, 'notfound': notfound})

    return render_to_response('department74/components_list.html', {'errors': errors, 'components': components})

    # return render(request, 'department74/components_list.html', {'components': components})


def components_new(request):
    if request.method == "POST":
        form = ComponentsForm(request.POST)
        if form.is_valid():
            new_component = form.save()
            # new_component.name = request.name
            # new_component.type_name = request.type_name
            # new_component.serial_number = request.serial_number
            # new_component.country = request.country
            # new_component.date_of_arrival = timezone.now()
            new_component.save()
            return redirect('/components/new/')
    else:
        form = ComponentsForm()
    return render(request, 'department74/components_new.html', context={'form': form})


def search(request):
    errors = []
    notfound = ''
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Введите поисковый запрос!')
        elif len(q) > 50:
            errors.append('Дохрена символов!')
        else:
            names = Components.objects.filter(name__icontains=q)
            serials = Components.objects.filter(serial_number__icontains=q)
            types = Components.objects.filter(name_type__name_type__icontains=q)
            matches = list(serials) + list(names) + list(types)
            if not matches:
                notfound = 'Ничего не найдено'
            return render_to_response('department74/search.html', {'matches': matches, 'query': q, 'notfound': notfound})
    return render_to_response('department74/search.html', {'errors': errors})
