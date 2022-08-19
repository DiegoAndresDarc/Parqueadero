from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from security_guard.models import Visitor, SecurityGuard
from security_guard.forms import GetVisitorFromIdentificationForm, CreateVisitorForm
from . import is_security_guard
from ..models import Shift


@login_required
@user_passes_test(is_security_guard)
def visitor_identification(request, action):
    """
    :param action:
    :param request:
    :return render:
    """
    security_guard = get_object_or_404(SecurityGuard, user=request.user)
    co_ownership = security_guard.co_ownership
    shift_started = False
    try:
        last_shift = Shift.objects.latest('id')
        if last_shift.end_date is None:
            shift_started = True
    except Shift.DoesNotExist:
        pass

    context = {
        'co_ownership': co_ownership,
        'shift_started': shift_started,
        'action': action
    }
    if request.method == 'POST':
        form = GetVisitorFromIdentificationForm(request.POST)
        if form.is_valid():
            identification = form.cleaned_data['identification']
            visitor = Visitor.objects.filter(identification=identification)
            if len(visitor) == 0:
                if action == 'departure':
                    context['action'] = ' visitor not registered'
                    return render(request, 'security_guard/parking_use.html', context)
                return HttpResponseRedirect(reverse('visitorCreate'))
            else:
                return HttpResponseRedirect(reverse('visitorVehicles', kwargs={'pk': visitor[0].id, 'action': action}))
    else:
        form = GetVisitorFromIdentificationForm()
    context['form'] = form
    return render(request, 'security_guard/visitor_identification.html', context)


@login_required
@user_passes_test(is_security_guard)
def create_visitor(request):
    """
    :param request:
    :return: render
    """
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = CreateVisitorForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            security_guard = get_object_or_404(SecurityGuard, user=request.user)
            co_ownership = security_guard.co_ownership
            visitor = form.save(commit=False)
            visitor.co_ownership = co_ownership
            visitor.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('visitorVehicles', kwargs={'pk': visitor.pk}))
            # If this is a GET (or any other method) create the default form.
    else:
        form = CreateVisitorForm()
    return render(request, 'security_guard/visitor_form.html', {'form': form})
