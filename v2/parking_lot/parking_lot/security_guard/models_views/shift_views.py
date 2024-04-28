from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from security_guard.models import Shift, SecurityGuard
from . import is_security_guard


@login_required
@user_passes_test(is_security_guard)
def start_shift(request, action):
    """
    :param action:
    :param request:
    :return render:
    """
    security_guard = get_object_or_404(SecurityGuard, user=request.user)
    shift = Shift()
    shift.security_guard = security_guard
    context = {
        'co_ownership': security_guard.co_ownership,
        'action': action
    }
    try:
        last_shift = Shift.objects.latest('id')
        if last_shift.end_date is None:
            return render(request, 'security_guard/shift_error.html', context=context)
        money = last_shift.final_money
    except Shift.DoesNotExist:
        money = 0
    shift.starting_money = money
    shift.final_money = money
    shift.save()
    context['money'] = money
    context['shift_started'] = True
    return render(request, 'security_guard/shift.html', context=context)


@login_required
@user_passes_test(is_security_guard)
def end_shift(request, action):
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
    try:
        last_shift = Shift.objects.filter(security_guard=security_guard).latest('id')
        if last_shift.end_date is not None:
            return render(request, 'security_guard/shift_error.html', {'action': action})
        last_shift.end_date = timezone.now()
        money = last_shift.final_money
        last_shift.save()
    except Shift.DoesNotExist:
        context['action'] = 'error'
        return render(request, 'security_guard/shift_error.html', context=context)
    context['money'] = money
    context['shift_started'] = False
    return render(request, 'security_guard/shift.html', context=context)
