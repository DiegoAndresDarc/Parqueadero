from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from admin_co_ownership.models import Inhabitant, InhabitantPayments, CoOwnership
from admin_co_ownership.forms import InhabitantPaymentForm

from . import is_admins_co_ownerships
from ..models import Configuration


@login_required
@user_passes_test(is_admins_co_ownerships)
def create_payment(request):
    """
    :param request:
    :return: render
    """
    co_ownership = get_object_or_404(CoOwnership, administrator=request.user)
    co_ownership_id = co_ownership.id
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = InhabitantPaymentForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            payment = form.save()
            inhabitant = payment.inhabitant
            inhabitant.up_to_date = True
            inhabitant.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('adminHome'))
            # If this is a GET (or any other method) create the default form.
    else:
        form = InhabitantPaymentForm(co_ownership_id=co_ownership_id)
        configuration = Configuration.objects.filter(co_ownership=co_ownership)
        context = {
            'co_ownership': co_ownership,
            'configured': len(configuration) > 0,
            'id_configuration': configuration[0].id if len(configuration) else 0,
            'form': form
        }
    return render(request, 'admin_co_ownership/inhabitantpayments_form.html', context)

