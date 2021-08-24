def is_admins_co_ownerships(user):
    return user.groups.filter(name='admins_co_ownerships').exists()
