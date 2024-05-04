from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import datetime

from admin_co_ownership.models import CoOwnership, Person, Vehicle, InhabitantVehicle, Apartment


# Create your models here.
class SecurityGuard(models.Model):
    """
    Clase para manejar los guardias de seguridad
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    co_ownership = models.ForeignKey(CoOwnership, on_delete=models.CASCADE, null=False)


class Visitor(models.Model):
    """
    Clase para administrar la información de los visitantes de la copropiedad
    """
    co_ownership = models.ForeignKey(CoOwnership, on_delete=models.CASCADE, null=False)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, null=False, verbose_name='Apartamento')

    def get_absolute_url(self):
        return reverse('visitor-detail', args=[str(self.id)])


class VisitorVehicle(models.Model):
    # Clase para administrar la información de los vehículos de los visitantes
    owner = models.ForeignKey(Visitor, on_delete=models.CASCADE, null=True, verbose_name='Propietario')
    plate = models.CharField(max_length=8, null=False, verbose_name="Número de placa")
    VEHICLE_TYPES = (
        ('C', 'Carro'),
        ('M', 'Moto'),
        ('B', 'Bicicleta')
    )

    type = models.CharField(max_length=1, choices=VEHICLE_TYPES, null=False, verbose_name="Tipo de vehiculo")

    def get_absolute_url(self):
        return reverse('visitor-vehicle-detail', args=[str(self.id)])


class VisitorsPayments(models.Model):
    """
    Clase para administrar los pagos de los visitantes
    """

    # Fields
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE, null=False, verbose_name='Visitante')
    payment_date = models.DateTimeField(null=False, default=datetime.now, verbose_name='Fecha del pago')
    value = models.DecimalField(decimal_places=2, max_digits=10, null=False, verbose_name='Valor del pago')


class Shift(models.Model):
    """
    Clase para administrar los turnos de los guardias de seguridad
    """

    # Fields
    security_guard = models.ForeignKey(SecurityGuard, on_delete=models.CASCADE, null=False)
    start_date = models.DateTimeField(null=False, default=datetime.now, verbose_name='Fecha de inicio del turno')
    end_date = models.DateTimeField(null=True, verbose_name='Fecha de fin del turno')
    starting_money = models.DecimalField(decimal_places=2, max_digits=10, null=False, verbose_name='Dinero inicial')
    final_money = models.DecimalField(decimal_places=2, max_digits=10, null=False, verbose_name='Dinero final')


class ParkingUseRecord(models.Model):

    class Meta:
        abstract = True

    # Fields
    entry_date = models.DateTimeField(null=False, default=datetime.now, verbose_name='Fecha y hora de ingreso')
    departure_date = models.DateTimeField(null=True, verbose_name='Fecha y hora de salida')


class VisitorParkingUse(ParkingUseRecord):

    # Fields
    vehicle = models.ForeignKey(VisitorVehicle, on_delete=models.CASCADE, null=False, verbose_name='Vehículo')


class InhabitantParkingUse(ParkingUseRecord):

    # Fields
    vehicle = models.ForeignKey(InhabitantVehicle, on_delete=models.CASCADE, null=False, verbose_name='Vehículo')
