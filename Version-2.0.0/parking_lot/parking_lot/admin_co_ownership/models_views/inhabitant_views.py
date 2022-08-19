from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from admin_co_ownership.models import Inhabitant, CoOwnership
from . import is_admins_co_ownerships
from ..models import Configuration


class InhabitantCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Inhabitant
    fields = '__all__'

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(InhabitantCreate, self).get_context_data(*args, **kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        configuration = Configuration.objects.filter(co_ownership=co_ownership)
        context['configured'] = len(configuration) > 0
        context['id_configuration'] = configuration[0].id if len(configuration) else 0
        return context


class InhabitantListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Inhabitant
    paginate_by = 10

    def get_queryset(self):
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        return Inhabitant.objects.filter(apartment__co_ownership=co_ownership)

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(InhabitantListView, self).get_context_data(*args, **kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        configuration = Configuration.objects.filter(co_ownership=co_ownership)
        context['configured'] = len(configuration) > 0
        context['id_configuration'] = configuration[0].id if len(configuration) else 0
        return context


class InhabitantDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Inhabitant

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(InhabitantDetailView, self).get_context_data(*args, **kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        configuration = Configuration.objects.filter(co_ownership=co_ownership)
        context['configured'] = len(configuration) > 0
        context['id_configuration'] = configuration[0].id if len(configuration) else 0
        return context


class InhabitantUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Inhabitant
    fields = '__all__'

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(InhabitantUpdate, self).get_context_data(*args, **kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        configuration = Configuration.objects.filter(co_ownership=co_ownership)
        context['configured'] = len(configuration) > 0
        context['id_configuration'] = configuration[0].id if len(configuration) else 0
        return context


class InhabitantDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Inhabitant
    success_url = reverse_lazy('adminHome')

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(InhabitantDelete, self).get_context_data(*args, **kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        configuration = Configuration.objects.filter(co_ownership=co_ownership)
        context['configured'] = len(configuration) > 0
        context['id_configuration'] = configuration[0].id if len(configuration) else 0
        return context


