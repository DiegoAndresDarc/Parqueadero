from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from security_guard.models import Visitor, SecurityGuard, Shift, VisitorVehicle
from security_guard.forms import CreateVisitorForm, CreateVisitorVehicleForm
from . import is_security_guard, set_default_context


@login_required
@user_passes_test(is_security_guard)
def visitor_identification(request, action):
    """
    :param action:
    :param request:
    :return render:
    """
    context = set_default_context(request.user)
    if not context['shift_started']:
        context['action'] = 'error'
        return render(request, 'security_guard/shift_error.html', context=context)

    context['action'] = action
    if request.method == 'POST':
        visitor_form = CreateVisitorForm(request.POST)
        vehicule_form = CreateVisitorVehicleForm(request.POST)
        if visitor_form.is_valid() and vehicule_form.is_valid():
            apartment = visitor_form.cleaned_data['apartment']
            visitor = Visitor.objects.filter(apartment=apartment)
            if len(visitor) == 0:
                if action == 'departure':
                    context['action'] = ' visitor not registered'
                    return render(request, 'security_guard/parking_use.html', context=context)
                visitor = create_visitor(visitor_form)
            else:
                visitor = visitor[0]
            vehicule_plate = vehicule_form.cleaned_data['plate']
            vehicule = VisitorVehicle.objects.filter(owner=visitor, plate=vehicule_plate)
            if len(vehicule) == 0:
                vehicule = create_vehicule(vehicule_form, visitor)
            else:
                vehicule = vehicule[0]
            if action == 'entry':
                return HttpResponseRedirect(reverse('barcodeVEntry', kwargs={'pk': vehicule.id}))
            return HttpResponseRedirect(reverse('barcodeVDeparture', kwargs={'pk': vehicule.id}))
    else:
        visitor_form = CreateVisitorForm()
        vehicule_form = CreateVisitorVehicleForm()
    context['visitor_form'] = visitor_form
    context['vehicule_form'] = vehicule_form
    return render(request, 'security_guard/visitor_identification.html', context=context)


def create_visitor(form):
    """
    :param form:
    :return: render
    """
    apartment = form.cleaned_data['apartment']
    visitor = form.save(commit=False)
    visitor.co_ownership = apartment.co_ownership
    visitor.save()
    return visitor


def create_vehicule(form, owner):
    """
    :param form:
    :param owner:
    :return: render
    """
    vehicule = form.save(commit=False)
    vehicule.owner = owner
    vehicule.save()
    return vehicule

