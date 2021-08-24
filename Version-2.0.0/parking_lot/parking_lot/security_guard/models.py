from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

from admin_co_ownership.models import CoOwnership, Person, Vehicle, InhabitantVehicle


# Create your models here.
class SecurityGuard(models.Model):
    """
    Clase para manejar los guardias de seguridad
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    co_ownership = models.ForeignKey(CoOwnership, on_delete=models.CASCADE, null=False)


class Visitor(Person):
    """
    Clase para administrar la información de los visitantes de la copropiedad
    """
    co_ownership = models.ForeignKey(CoOwnership, on_delete=models.CASCADE, null=False)

    def get_absolute_url(self):
        return reverse('visitor-detail', args=[str(self.id)])


class VisitorVehicle(Vehicle):
    # Clase para administrar la información de los vehículos de los visitantes
    owner = models.ForeignKey(Visitor, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse('visitor-vehicle-detail', args=[str(self.id)])


class VisitorsPayments(models.Model):
    """
    Clase para administrar los pagos de los visitantes
    """

    # Fields
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE, null=False)
    payment_date = models.DateTimeField(null=False, default=timezone.now, verbose_name='Fecha del pago')
    value = models.DecimalField(decimal_places=2, max_digits=5, null=False, verbose_name='Valor del pago')


class Shift(models.Model):
    """
    Clase para administrar los turnos de los guardias de seguridad
    """

    # Fields
    security_guard = models.ForeignKey(SecurityGuard, on_delete=models.CASCADE, null=False)
    start_date = models.DateTimeField(null=False, default=timezone.now, verbose_name='Fecha de inicio del turno')
    end_date = models.DateTimeField(null=True, verbose_name='Fecha de fin del turno')
    starting_money = models.DecimalField(decimal_places=2, max_digits=10, null=False, verbose_name='Dinero inicial')
    final_money = models.DecimalField(decimal_places=2, max_digits=10, null=False, verbose_name='Dinero final')


class ParkingUseRecord(models.Model):

    class Meta:
        abstract = True

    # Fields
    entry_date = models.DateTimeField(null=False, default=timezone.now, verbose_name='Fecha de ingreso')
    departure_date = models.DateTimeField(null=True, verbose_name='Fecha y hora de salida')


class VisitorParkingUse(ParkingUseRecord):

    # Fields
    vehicle = models.ForeignKey(VisitorVehicle, on_delete=models.CASCADE, null=False)


class InhabitantParkingUse(ParkingUseRecord):

    # Fields
    vehicle = models.ForeignKey(InhabitantVehicle, on_delete=models.CASCADE, null=False)
