from django.contrib import admin
from .models import Visitor, VisitorVehicle, VisitorsPayments, Shift, SecurityGuard, VisitorParkingUse, InhabitantParkingUse
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


# Register your models here.
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class SecurityGuardInline(admin.StackedInline):
    model = SecurityGuard
    can_delete = False
    verbose_name_plural = 'security guards'


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    pass


@admin.register(VisitorVehicle)
class VisitorVehicleAdmin(admin.ModelAdmin):
    pass


@admin.register(VisitorsPayments)
class VisitorsPaymentsAdmin(admin.ModelAdmin):
    pass

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    pass


@admin.register(VisitorParkingUse)
class VisitorParkingUseAdmin(admin.ModelAdmin):
    pass


@admin.register(InhabitantParkingUse)
class InhabitantParkingUseAdmin(admin.ModelAdmin):
    pass


class UserAdmin(BaseUserAdmin):
    inlines = (SecurityGuardInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
