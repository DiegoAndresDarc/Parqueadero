from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from admin_co_ownership.models import ParkingPlace, CoOwnership
from admin_co_ownership.forms import CreateParkingPlaceForm
from . import is_admins_co_ownerships


@login_required
@user_passes_test(is_admins_co_ownerships)
def create_parking_place(request):
    """
    :param request:
    :return:
    """
    co_ownership = get_object_or_404(CoOwnership, administrator=request.user)
    if request.method == 'POST':
        form = CreateParkingPlaceForm(request.POST)
        if form.is_valid():
            parking_place = form.save(commit=False)
            parking_place.co_ownership = co_ownership
            parking_place.save()
            return HttpResponseRedirect(reverse('adminHome'))
    else:
        form = CreateParkingPlaceForm()
    context = {'form': form, 'co_ownership': co_ownership}
    return render(request, 'admin_co_ownership/parkingplace_form.html', context=context)


class ParkingPlaceListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = ParkingPlace
    paginate_by = 10

    def get_queryset(self):
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        return ParkingPlace.objects.filter(co_ownership=co_ownership)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ParkingPlaceListView, self).get_context_data(**kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        return context

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)


class ParkingPlaceDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = ParkingPlace

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ParkingPlaceDetailView, self).get_context_data(**kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        return context

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)


class ParkingPlaceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ParkingPlace
    fields = ['code', 'area', 'admitted_weight', 'admitted_axis', 'barcode', 'supports_car', 'supports_motorcycle',
              'supports_bicycle', 'user_type', 'in_use']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ParkingPlaceUpdateView, self).get_context_data(**kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        return context

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)


class ParkingPlaceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ParkingPlace
    success_url = reverse_lazy('adminHome')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ParkingPlaceDeleteView, self).get_context_data(**kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        return context

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)


