from django.shortcuts import get_object_or_404
from admin_co_ownership.models import CoOwnership, Configuration


def is_admins_co_ownerships(user):
    return user.groups.filter(name='admins_co_ownerships').exists()


def set_default_context(user, context):
    co_ownership = get_object_or_404(CoOwnership, administrator=user)
    configuration = Configuration.objects.filter(co_ownership=co_ownership)
    if context is not None:
        context['co_ownership'] = co_ownership
        context['configured'] = len(configuration) > 0
        context['id_configuration'] = configuration[0].id if len(configuration) else 0
    else:
        context = {
            'co_ownership': co_ownership,
            'configured': len(configuration) > 0,
            'id_configuration': configuration[0].id if len(configuration) else 0
        }
    return context
