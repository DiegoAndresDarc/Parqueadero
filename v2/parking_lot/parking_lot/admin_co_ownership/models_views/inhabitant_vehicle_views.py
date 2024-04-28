from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from admin_co_ownership.models import InhabitantVehicle, CoOwnership
from admin_co_ownership.forms import InhabitantVehicleForm
from . import is_admins_co_ownerships


@login_required
@user_passes_test(is_admins_co_ownerships)
def create_vehicle(request):
    """
    :param request:
    :return: render
    """
    co_ownership = get_object_or_404(CoOwnership, administrator=request.user)
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = InhabitantVehicleForm(request.POST, request.FILES)
        # Check if the form is valid:
        if form.is_valid():
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('adminHome'))
            # If this is a GET (or any other method) create the default form.
    else:
        form = InhabitantVehicleForm(co_ownership_id=co_ownership.id)
    context = {'form': form, 'co_ownership': co_ownership}
    return render(request, 'admin_co_ownership/inhabitantvehicle_form.html', context=context)


class InhabitantVehicleListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = InhabitantVehicle
    paginate_by = 10

    def get_queryset(self):
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        return InhabitantVehicle.objects.filter(owner__apartment__co_ownership=co_ownership)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(InhabitantVehicleListView, self).get_context_data(**kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        return context

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)


class InhabitantVehicleDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = InhabitantVehicle

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(InhabitantVehicleDetailView, self).get_context_data(**kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        return context

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)


class InhabitantVehicleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = InhabitantVehicle
    fields = '__all__'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(InhabitantVehicleUpdateView, self).get_context_data(**kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        return context

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)


class InhabitantVehicleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = InhabitantVehicle
    success_url = reverse_lazy('adminHome')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(InhabitantVehicleDeleteView, self).get_context_data(**kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        return context

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)


class SetParkingPlaceView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = InhabitantVehicle
    fields = ['parking_place']
    success_url = reverse_lazy('setParkingPlace')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SetParkingPlaceView, self).get_context_data(**kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        return context

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)

