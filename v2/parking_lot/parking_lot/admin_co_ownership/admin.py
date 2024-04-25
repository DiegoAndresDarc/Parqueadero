from django.contrib import admin
from .models import CoOwnership, Configuration, ParkingPlace, Inhabitant, InhabitantVehicle, Apartment


class CoOwnershipInLine(admin.TabularInline):
    model = CoOwnership
    extra = 0
    max_num = 1


class ConfigurationInLine(admin.StackedInline):
    model = Configuration
    extra = 0
    max_num = 1


@admin.register(CoOwnership)
class CoOwnershipAdmin(admin.ModelAdmin):
    list_display = ('name', 'administrator', 'address', 'enable')
    list_filter = ('enable',)
    fields = ['name', 'address', 'administrator', 'enable']
    inlines = [ConfigurationInLine]


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('CONFIGURACIÓN BÁSICA', {
            'fields': ('co_ownership', ('max_weight', 'max_axis'), ('arching_day', 'alerts_day'))
        }),
        ('CONFIGURACIÓN DE PARQUEADEROS', {
            'fields': (('car_parking_num', 'motorcycle_parking_num', 'bicycle_parking_num'), ('visit_car_parking_num',
                                                                                              'visit_motorcycle_parking_num',
                                                                                              'visit_bicycle_parking_num'))
        }),
        ('CONFIGURACIÓN DE PAGOS', {
            'fields': (('visit_payment_type', 'grace_time'),
                       ('car_payment_value', 'motorcycle_payment_value', 'bicycle_payment_value'))
        }),
        ('CONFIGURACIÓN DE RECIBOS DE PAGO', {
            'fields': ('receipt_header', 'receipt_footer', 'responsibility_text')
        })
    )


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Inhabitant)
class InhabitantAdmin(admin.ModelAdmin):
    pass


@admin.register(ParkingPlace)
class ParkingPlaceAdmin(admin.ModelAdmin):
    pass


@admin.register(InhabitantVehicle)
class VehicleAdmin(admin.ModelAdmin):
    pass
