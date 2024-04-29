from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from security_guard.models import Visitor, SecurityGuard, Shift
from security_guard.forms import GetVisitorFromIdentificationForm, CreateVisitorForm
from . import is_security_guard


@login_required
@user_passes_test(is_security_guard)
def visitor_identification(request, action):
    """
    :param action:
    :param request:
    :return render:
    """
    security_guard = get_object_or_404(SecurityGuard, user=request.user)
    context = {
        'co_ownership': security_guard.co_ownership,
        'action': action
    }
    shift_started = False
    try:
        last_shift = Shift.objects.latest('id')
        if last_shift.end_date is None:
            shift_started = True
    except Shift.DoesNotExist:
        pass
    if not shift_started:
        context['action'] = 'error'
        return render(request, 'security_guard/shift_error.html', context=context)
    context['shift_started'] = shift_started

    if request.method == 'POST':
        form = GetVisitorFromIdentificationForm(request.POST)
        if form.is_valid():
            identification = form.cleaned_data['identification']
            visitor = Visitor.objects.filter(identification=identification)
            if len(visitor) == 0:
                if action == 'departure':
                    context['action'] = ' visitor not registered'
                    return render(request, 'security_guard/parking_use.html', context=context)
                return HttpResponseRedirect(reverse('visitorCreate'))
            else:
                return HttpResponseRedirect(reverse(
                    'visitorVehicles',
                    kwargs={
                        'pk': visitor[0].id,
                        'action': action
                    }))
    else:
        form = GetVisitorFromIdentificationForm()
    context['form'] = form
    return render(request, 'security_guard/visitor_identification.html', context=context)


@login_required
@user_passes_test(is_security_guard)
def create_visitor(request):
    """
    :param request:
    :return: render
    """
    security_guard = get_object_or_404(SecurityGuard, user=request.user)
    context = {
        'co_ownership': security_guard.co_ownership
    }
    shift_started = False
    try:
        last_shift = Shift.objects.latest('id')
        if last_shift.end_date is None:
            shift_started = True
    except Shift.DoesNotExist:
        pass
    if not shift_started:
        context['action'] = 'error'
        return render(request, 'security_guard/shift_error.html', context=context)
    context['shift_started'] = shift_started

    if request.method == 'POST':
        form = CreateVisitorForm(request.POST)
        if form.is_valid():
            security_guard = get_object_or_404(SecurityGuard, user=request.user)
            co_ownership = security_guard.co_ownership
            visitor = form.save(commit=False)
            visitor.co_ownership = co_ownership
            visitor.save()
            return HttpResponseRedirect(reverse(
                'visitorVehicles',
                kwargs={
                    'pk': visitor.pk, 'action': 'create'
                }))
    else:
        form = CreateVisitorForm()
    context['form'] = form
    return render(request, 'security_guard/visitor_form.html', context=context)
