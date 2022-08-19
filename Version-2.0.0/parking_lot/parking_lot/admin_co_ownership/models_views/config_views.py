from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView

from admin_co_ownership.forms import SetConfigurationForm, ModConfigurationForm
from admin_co_ownership.models import CoOwnership, Configuration
from . import is_admins_co_ownerships


@login_required
@user_passes_test(is_admins_co_ownerships)
def set_configuration(request):
    """
    :param request:
    :return: render
    """
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = SetConfigurationForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            co_ownership = get_object_or_404(CoOwnership, administrator=request.user)
            configuration = form.save(commit=False)
            configuration.co_ownership = co_ownership
            configuration.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('adminHome'))
            # If this is a GET (or any other method) create the default form.
    else:
        form = SetConfigurationForm()
    return render(request, 'admin_co_ownership/configuration_form.html', {'form': form})


@login_required
@user_passes_test(is_admins_co_ownerships)
def update_configuration(request, pk):
    """
    :param request:
    :param pk:
    :return:
    """
    configuration = get_object_or_404(Configuration, pk=pk)
    context = {}
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = ModConfigurationForm(request.POST, instance=configuration)
        # Check if the form is valid:
        if form.is_valid():
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('adminHome'))
            # If this is a GET (or any other method) create the default form.
    else:
        form = ModConfigurationForm(instance=configuration)
        co_ownership = get_object_or_404(CoOwnership, administrator=request.user)
        context = {
            'co_ownership': co_ownership,
            'configured': True,
            'id_configuration': pk,
            'form': form
        }
    return render(request, 'admin_co_ownership/configuration_form.html', context)


class ConfigurationDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Configuration
    success_url = reverse_lazy('adminHome')

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(ConfigurationDelete, self).get_context_data(*args, **kwargs)
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        context['co_ownership'] = co_ownership
        configuration = Configuration.objects.filter(co_ownership=co_ownership)
        context['configured'] = len(configuration) > 0
        context['id_configuration'] = configuration[0].id if len(configuration) else 0
        return context
