from django.shortcuts import render
from django.utils import timezone
from .models import Components
from .forms import ComponentsForm
from django.shortcuts import redirect


def ind(request):
    return render(request, 'department74/ind.html', {})


def arrival(request):
    return render(request, 'department74/arrival.html', {})


def components_list(request):
    components = Components.objects.filter(date_of_arrival__lte=timezone.now()).order_by('date_of_arrival')
    return render(request, 'department74/components_list.html', {'components': components})


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
