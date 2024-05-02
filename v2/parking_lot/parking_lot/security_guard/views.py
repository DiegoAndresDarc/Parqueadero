from .models_views.shift_views import *
from .models_views.parking_use_views import *
from .models_views.visitor_views import *
from .models import SecurityGuard, Shift


# Create your views here.
@login_required
@user_passes_test(is_security_guard)
def security_guard_home(request):
    """
    :param request:
    :return render:
    """
    security_guard = get_object_or_404(SecurityGuard, user=request.user)
    shift_started = False
    try:
        last_shift = Shift.objects.latest('id')
        if last_shift.end_date is None:
            shift_started = True
    except Shift.DoesNotExist:
        pass

    context = {
        'co_ownership': security_guard.co_ownership,
        'shift_started': shift_started
    }
    return render(request, 'securityGuardIndex.html', context=context)
