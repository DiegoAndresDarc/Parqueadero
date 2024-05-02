from django.shortcuts import get_object_or_404
from security_guard.models import SecurityGuard, Shift


def is_security_guard(user):
    return user.groups.filter(name='security_guards').exists()


def set_default_context(user, context=None):
    if context is None:
        context = {}
    security_guard = get_object_or_404(SecurityGuard, user=user)
    context['co_ownership'] = security_guard.co_ownership
    shift_started = False
    try:
        last_shift = Shift.objects.filter(security_guard=security_guard).latest('id')
        if last_shift.end_date is None:
            shift_started = True
    except Shift.DoesNotExist:
        pass
    context['shift_started'] = shift_started
    return context
