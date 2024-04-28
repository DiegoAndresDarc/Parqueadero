from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from admin_co_ownership.models import Inhabitant, CoOwnership
from . import is_admins_co_ownerships


class InhabitantCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Inhabitant
    fields = '__all__'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(InhabitantCreateView, self).get_context_data(**kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        return context

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)


class InhabitantListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Inhabitant
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(InhabitantListView, self).get_context_data(**kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        return context

    def get_queryset(self):
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        return Inhabitant.objects.filter(apartment__co_ownership=co_ownership)

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)


class InhabitantDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Inhabitant

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(InhabitantDetailView, self).get_context_data(**kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        return context

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)


class InhabitantUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Inhabitant
    fields = '__all__'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(InhabitantUpdateView, self).get_context_data(**kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        return context

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)


class InhabitantDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Inhabitant
    success_url = reverse_lazy('adminHome')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(InhabitantDeleteView, self).get_context_data(**kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        return context

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)


