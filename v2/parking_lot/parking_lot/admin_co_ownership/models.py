from django.db import models
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date


def photo_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/plate/photo_dd_MM_YYYY
    today = date.today().strftime('%d_%m_%Y')
    return '{0}/foto_{1}{2}'.format(instance.plate, today, filename[filename.rindex('.'):])


def property_letter_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/plate/property_letter_dd_MM_YYYY
    today = date.today().strftime('%d_%m_%Y')
    return '{0}/carta_de_propiedad_{1}{2}'.format(instance.plate, today, filename[filename.rindex('.'):])


def soat_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/plate/soat_dd_MM_YYYY
    today = date.today().strftime('%d_%m_%Y')
    return '{0}/soat_{1}{2}'.format(instance.plate, today, filename[filename.rindex('.'):])


class Person(models.Model):

    class Meta:
        abstract = True
        ordering = ['first_name', 'last_name']

    first_name = models.CharField(max_length=50, null=False, verbose_name="Nombres")
    last_name = models.CharField(max_length=50, null=False, verbose_name="Apellidos")

    IDENTIFICATIONS_TYPE = (
        ('CC', 'Cédula de ciudadanía'),
        ('CE', 'Cédula de extranjería')
    )

    identification_type = models.CharField(max_length=2, choices=IDENTIFICATIONS_TYPE, null=False, default='CC', verbose_name="Tipo de identificación")
    identification = models.BigIntegerField(null=False, unique=True, verbose_name="Documento de identificación")
    cellphone = models.BigIntegerField(null=False, verbose_name="Número de celular")

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)


class CoOwnership(models.Model):
    """
    Clase para administrar las copropiedades de la app.
    """
    # Fields
    administrator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30, null=False, verbose_name="Nombre")
    address = models.CharField(max_length=50, null=False, verbose_name="Dirección")
    enable = models.BooleanField(null=False, default=False, verbose_name="Habilitada")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('co-ownership-detail', args=[str(self.id)])


class Configuration(models.Model):
    """
    Clase para administrar la configuración de una copropiedad
    """
    co_ownership = models.ForeignKey(CoOwnership, on_delete=models.CASCADE, null=False)
    max_weight = models.DecimalField(decimal_places=2, max_digits=5, null=False, verbose_name="Peso máximo permitido para vehículos")
    max_axis = models.IntegerField(null=False, verbose_name="Ejes máximos permitidos para vehículos")
    DAYS = (
        ('L', 'Lunes'),
        ('M', 'Martes'),
        ('C', 'Miércoles'),
        ('J', 'Jueves'),
        ('V', 'Viernes'),
        ('S', 'Sábado'),
        ('D', 'Domingo'),
    )
    arching_day = models.CharField(max_length=1, choices=DAYS, null=False, verbose_name="Día de la semana para arqueo de caja")
    alerts_day = models.CharField(max_length=1, choices=DAYS, null=False, verbose_name="Día de la semana para enviar alertas")
    car_parking_num = models.IntegerField(null=False, default=0, verbose_name="Cantidad de parqueaderos para carros")
    motorcycle_parking_num = models.IntegerField(null=False, default=0, verbose_name="Cantidad de parqueaderos para motocicletas")
    bicycle_parking_num = models.IntegerField(null=False, default=0, verbose_name="Cantidad de parqueaderos para bicicletas")
    visit_car_parking_num = models.IntegerField(null=False, default=0, verbose_name="Cantidad de parqueaderos de carros para visitantes")
    visit_motorcycle_parking_num = models.IntegerField(null=False, default=0, verbose_name="Cantidad de parqueaderos de motocicletas para visitantes")
    visit_bicycle_parking_num = models.IntegerField(null=False, default=0, verbose_name="Cantidad de parqueaderos de bicicletas para visitantes")

    PAYMENT_TYPE = (
        ('H', 'Hora'),
        ('M', 'Minuto'),
        ('D', 'Día')
    )
    visit_payment_type = models.CharField(max_length=1, choices=PAYMENT_TYPE, null=False, verbose_name="Tipo de pago para visitantes")
    grace_time = models.DecimalField(decimal_places=2, max_digits=4, null=False, default=0.0, verbose_name="Tiempo de gracia para el periodo especificado")
    payment_value_after_one_day = models.DecimalField(decimal_places=2, max_digits=10, null=False, verbose_name="Valor extra a cobrar después de un dia de uso")
    car_payment_value = models.DecimalField(decimal_places=2, max_digits=10, null=False, verbose_name="Valor del pago para carros")
    motorcycle_payment_value = models.DecimalField(decimal_places=2, max_digits=10, null=False, verbose_name="Valor del pago para motocicletas")
    bicycle_payment_value = models.DecimalField(decimal_places=2, max_digits=10, null=False, verbose_name="Valor del pago para bicicletas")
    receipt_header = models.TextField(null=False, verbose_name="Encabezado del recibo de pago")
    receipt_footer = models.TextField(null=False, verbose_name="Pie de página del recibo de pago")
    responsibility_text = models.TextField(null=False, verbose_name="Texto de responsabilidad")

    def __str__(self):
        return '%s Configuration' % self.co_ownership.name

    def get_absolute_url(self):
        return reverse('adminHome')


class Apartment(models.Model):
    """
    Clase para administrar la información de los apartamentos de una copropiedad
    """
    # Fields
    co_ownership = models.ForeignKey(CoOwnership, on_delete=models.CASCADE, null=False)
    block = models.CharField(max_length=10, null=False, verbose_name="Número/Nombre del bloque")
    apartment = models.CharField(max_length=10, null=False, verbose_name="Número/Nombre del apartamento")

    class Meta:
        ordering = ['block', 'apartment']

    def __str__(self):
        return '%s %s' % (self.block, self.apartment)

    def get_absolute_url(self):
        return reverse('apartment-detail', args=[str(self.id)])


class Inhabitant(Person):
    """
    Clase para administrar la información de los residentes/habitantes de un apartamento
    """

    email = models.EmailField(null=False, verbose_name="Correo electrónico")
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, null=False, verbose_name="Apartamento")
    responsible = models.BooleanField(null=False, default=False, verbose_name="Es el responsable por el apartamento")
    up_to_date = models.BooleanField(default=False, verbose_name="Al día con pago del parqueadero")

    def get_absolute_url(self):
        return reverse('inhabitant-detail', args=[str(self.id)])


class ParkingPlace(models.Model):
    """
    Clase para administrar la información de un lugar de parqueo
    """
    # Fields
    co_ownership = models.ForeignKey(CoOwnership, on_delete=models.CASCADE, null=False)
    code = models.CharField(max_length=10, unique=True, null=False, verbose_name="Código de identificación")
    area = models.DecimalField(decimal_places=2, max_digits=4, null=False, verbose_name="Área")
    admitted_weight = models.DecimalField(decimal_places=2, max_digits=5, null=False, verbose_name="Peso máximo admitido")
    admitted_axis = models.IntegerField(null=False, verbose_name="Ejes máximos admitidos")
    barcode = models.CharField(max_length=20, unique=True, null=False, verbose_name="Código de barras del carnet")
    supports_car = models.BooleanField(null=False, default=False, verbose_name="Admite carros")
    supports_motorcycle = models.BooleanField(null=False, default=False, verbose_name="Admite motocicletas")
    supports_bicycle = models.BooleanField(null=False, default=False, verbose_name="Admite bicicletas")

    USERS_TYPE = (
        ('I', 'Residentes'),
        ('V', 'Visitantes'),
        ('M', 'MultiUso')
    )

    user_type = models.CharField(max_length=1, choices=USERS_TYPE, null=False, default='I', verbose_name="Para ser usado por")
    in_use = models.BooleanField(null=False, default=False, verbose_name="Parqueadero en uso")

    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse('parking-place-detail', args=[str(self.id)])


class Vehicle(models.Model):
    """
    Clase para administrar la información de los vehículos de los residentes
    """

    class Meta:
        abstract = True
        ordering = ['brand', 'model', 'type']

    # Fields
    parking_place = models.ForeignKey(ParkingPlace, on_delete=models.CASCADE, null=True, verbose_name="Parqueadero")
    brand = models.CharField(max_length=20, null=False, verbose_name="Marca del vehiculo")
    model = models.CharField(max_length=20, null=False, verbose_name="Modelo del vehiculo")

    VEHICLE_TYPES = (
        ('C', 'Carro'),
        ('M', 'Moto'),
        ('B', 'Bicicleta')
    )

    type = models.CharField(max_length=1, choices=VEHICLE_TYPES, null=False, verbose_name="Tipo de vehiculo")
    color = models.CharField(max_length=10, null=False, verbose_name="Color")
    weight = models.DecimalField(decimal_places=2, max_digits=5, null=False, verbose_name="Peso")
    axis = models.IntegerField(null=False, verbose_name="Número de ejes")
    plate = models.CharField(max_length=8, null=False, verbose_name="Número de placa")
    picture = models.ImageField(upload_to=photo_directory_path, null=False, verbose_name="Foto a color")

    def __str__(self):
        return '%s: %s %s %s' % (self.type, self.brand, self.model, self.color)


class InhabitantVehicle(Vehicle):
    """
    Clase para administrar los vehículos de los habitantes de la copropiedad
    """
    owner = models.ForeignKey(Inhabitant, on_delete=models.CASCADE, null=False, verbose_name="Propietario")
    property_letter = models.FileField(upload_to=property_letter_directory_path, null=False, verbose_name="Carta de propiedad")
    soat = models.FileField(upload_to=soat_directory_path, null=True, verbose_name="Soporte del SOAT")
    due_date = models.DateField(null=True, verbose_name="Fecha de vencimiento del SOAT")

    def get_absolute_url(self):
        return reverse('vehicle-detail', args=[str(self.id)])


class InhabitantPayments(models.Model):
    """
    Clase para administrar los pagos de los visitantes
    """

    # Fields
    inhabitant = models.ForeignKey(Inhabitant, on_delete=models.CASCADE, null=False, verbose_name="Residente")
    payment_date = models.DateTimeField(null=False, default=timezone.now, verbose_name="Fecha del pago")

    def get_absolute_url(self):
        return reverse('payment-detail', args=[str(self.id)])
