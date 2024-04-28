from django.contrib.auth.models import Group
from .forms import SecurityGuardForm
from .models_views.config_views import *
from .models_views.apartment_views import *
from .models_views.inhabitant_views import *
from .models_views.parking_place_views import *
from .models_views.inhabitant_vehicle_views import *
from .models_views.payment_views import *
from .models_views.security_guard_views import *


# Create your models_views here.
@login_required
@user_passes_test(is_admins_co_ownerships)
def admin_home(request):
    """
    Página de inicio del administrador
    :param request:
    :return: render
    """

    co_ownership = get_object_or_404(CoOwnership, administrator=request.user)
    configuration = Configuration.objects.filter(co_ownership=co_ownership)

    context = {
        'co_ownership': co_ownership,
        'configured': len(configuration) > 0,
        'id_configuration': configuration[0].id if len(configuration) else 0
    }
    return render(request, 'adminIndex.html', context)


@login_required
@user_passes_test(is_admins_co_ownerships)
def inhabitant_vehicles(request, action):
    """
    :param request:
    :param action:
    :return: render
    """
    co_ownership = get_object_or_404(CoOwnership, administrator=request.user)
    inhabitantvehicle_list = InhabitantVehicle.objects.filter(owner__apartment__co_ownership=co_ownership)

    context = {
        'co_ownership': co_ownership,
        'action': action,
        'inhabitantvehicle_list': inhabitantvehicle_list
    }
    return render(request, 'admin_co_ownership/inhabitantvehicles.html', context=context)


@login_required
@user_passes_test(is_admins_co_ownerships)
def remove_parking_place_to_vehicle(request, pk):
    """
    :param request:
    :return:
    """
    vehicle = get_object_or_404(InhabitantVehicle, pk=pk)
    vehicle.parking_place = None
    vehicle.save()
    co_ownership = get_object_or_404(CoOwnership, administrator=request.user)

    context = {
        'co_ownership': co_ownership,
        'action': 'remove'
    }
    return inhabitant_vehicles(request, context=context)
