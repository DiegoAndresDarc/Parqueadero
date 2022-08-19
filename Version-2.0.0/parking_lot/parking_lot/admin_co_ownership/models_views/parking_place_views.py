from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from admin_co_ownership.models import ParkingPlace, CoOwnership
from admin_co_ownership.forms import CreateParkingPlaceForm
from . import is_admins_co_ownerships
from ..models import Configuration


@login_required
@user_passes_test(is_admins_co_ownerships)
def create_parking_place(request):
    """
    :param request:
    :return:
    """
    co_ownership = get_object_or_404(CoOwnership, administrator=request.user)
    context = {}
    if request.method == 'POST':
        form = CreateParkingPlaceForm(request.POST)
        if form.is_valid():
            parking_place = form.save(commit=False)
            parking_place.co_ownership = co_ownership
            parking_place.save()
            return HttpResponseRedirect(reverse('adminHome'))
    else:
        form = CreateParkingPlaceForm()
        configuration = Configuration.objects.filter(co_ownership=co_ownership)
        context = {
            'co_ownership': co_ownership,
            'configured': len(configuration) > 0,
            'id_configuration': configuration[0].id if len(configuration) else 0,
            'form': form
        }
    return render(request, 'admin_co_ownership/parkingplace_form.html', context)


class ParkingPlaceListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = ParkingPlace
    paginate_by = 10

    def get_queryset(self):
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        return ParkingPlace.objects.filter(co_ownership=co_ownership)

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(ParkingPlaceListView, self).get_context_data(*args, **kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        configuration = Configuration.objects.filter(co_ownership=co_ownership)
        context['configured'] = len(configuration) > 0
        context['id_configuration'] = configuration[0].id if len(configuration) else 0
        return context


class ParkingPlaceDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = ParkingPlace

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(ParkingPlaceDetailView, self).get_context_data(*args, **kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        configuration = Configuration.objects.filter(co_ownership=co_ownership)
        context['configured'] = len(configuration) > 0
        context['id_configuration'] = configuration[0].id if len(configuration) else 0
        return context


class ParkingPlaceUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ParkingPlace
    fields = ['code', 'area', 'admitted_weight', 'admitted_axis', 'barcode', 'supports_car', 'supports_motorcycle',
              'supports_bicycle', 'user_type', 'in_use']

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(ParkingPlaceUpdate, self).get_context_data(*args, **kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        configuration = Configuration.objects.filter(co_ownership=co_ownership)
        context['configured'] = len(configuration) > 0
        context['id_configuration'] = configuration[0].id if len(configuration) else 0
        return context


class ParkingPlaceDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ParkingPlace
    success_url = reverse_lazy('adminHome')

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(ParkingPlaceDelete, self).get_context_data(*args, **kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        configuration = Configuration.objects.filter(co_ownership=co_ownership)
        context['configured'] = len(configuration) > 0
        context['id_configuration'] = configuration[0].id if len(configuration) else 0
        return context
