from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from admin_co_ownership.forms import CreateApartmentForm
from admin_co_ownership.models import CoOwnership, Apartment
from . import is_admins_co_ownerships


@login_required
@user_passes_test(is_admins_co_ownerships)
def create_apartment(request):
    """
    :param request:
    :return: render
    """
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = CreateApartmentForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            co_ownership = get_object_or_404(CoOwnership, administrator=request.user)
            apartment = form.save(commit=False)
            apartment.co_ownership = co_ownership
            apartment.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('adminHome'))
            # If this is a GET (or any other method) create the default form.
    else:
        form = CreateApartmentForm()
    return render(request, 'admin_co_ownership/apartment_form.html', {'form': form})


class ApartmentListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Apartment
    paginate_by = 10

    def get_queryset(self):
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        return Apartment.objects.filter(co_ownership=co_ownership)

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)


class ApartmentDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Apartment

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)


class ApartmentUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Apartment
    fields = ['block', 'apartment']

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)


class ApartmentDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Apartment
    success_url = reverse_lazy('adminHome')

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)

