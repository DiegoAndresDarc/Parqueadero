from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect


def home(request):
    """
    Página de inicio del administrador
    :param request:
    :return: render
    """
    if request.user is None or request.user.is_anonymous:
        return HttpResponseRedirect(reverse('login'))
    else:
        if request.user.is_superuser:
            return redirect('/admin')
        group = request.user.groups.all()[0]
        if 'admins_co_ownerships' in group.name:
            return HttpResponseRedirect(reverse('adminHome'))
        elif 'security_guards' in group.name:
            return HttpResponseRedirect(reverse('securityGuardHome'))
        else:
            return HttpResponseRedirect(reverse('login'))

