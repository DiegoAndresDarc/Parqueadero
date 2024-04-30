from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView

from . import is_admins_co_ownerships, set_default_context
from admin_co_ownership.forms import SecurityGuardForm
from admin_co_ownership.models import CoOwnership
from security_guard.models import SecurityGuard


@login_required
@user_passes_test(is_admins_co_ownerships)
def create_security_guard(request):
    """
    :param request:
    :return:
    """
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = SecurityGuardForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            co_ownership = get_object_or_404(CoOwnership, administrator=request.user)
            user = form.save()
            group = Group.objects.get(name='security_guards')
            group.user_set.add(user)
            group.save()
            security_guard = SecurityGuard()
            security_guard.user = user
            security_guard.co_ownership = co_ownership
            security_guard.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('adminHome'))
    else:
        form = SecurityGuardForm()
    context = set_default_context(request.user, None)
    context['form'] = form
    return render(request, 'admin_co_ownership/securityguard_form.html', context=context)


class SecurityGuardListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = SecurityGuard
    paginate_by = 10

    def get_queryset(self):
        co_ownership = get_object_or_404(CoOwnership, administrator=self.request.user)
        return SecurityGuard.objects.filter(co_ownership=co_ownership)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SecurityGuardListView, self).get_context_data(**kwargs)
        set_default_context(self.request.user, context)
        return context

    def test_func(self):
        return is_admins_co_ownerships(self.request.user)


@login_required
@user_passes_test(is_admins_co_ownerships)
def delete_security_guard(request, pk):
    """
    :param request:
    :param pk:
    :return:
    """
    security_guard = get_object_or_404(SecurityGuard, pk=pk)
    user = security_guard.user
    security_guard.delete()
    user.delete()
    return HttpResponseRedirect(reverse('adminHome'))
