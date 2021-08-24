def is_security_guard(user):
    return user.groups.filter(name='security_guards').exists()
