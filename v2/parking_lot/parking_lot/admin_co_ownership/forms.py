import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _

from .models import Apartment, Configuration, ParkingPlace, InhabitantVehicle, InhabitantPayments, Inhabitant, CoOwnership


class SetConfigurationForm(ModelForm):
    class Meta:
        model = Configuration
        exclude = ['co_ownership', ]

    def __init__(self, *args, **kwargs):
        super(SetConfigurationForm, self).__init__(*args, **kwargs)

    def clean_max_weight(self):
        data = self.cleaned_data['max_weight']

        if data < 0:
            raise ValidationError(_('Max weight cannot be less than 0'))
        # Remember to always return the cleaned data.
        return data

    def clean_max_axis(self):
        data = self.cleaned_data['max_axis']

        if data < 0:
            raise ValidationError(_('Max axis cannot be less than 0'))
        if data > 10:
            raise ValidationError(_('Max axis cannot be greater than 10'))
        # Remember to always return the cleaned data.
        return data

    def clean_car_parking_num(self):
        data = self.cleaned_data['car_parking_num']

        if data < 0:
            raise ValidationError(_('Car parking spaces cannot be less than 0'))
        # Remember to always return the cleaned data.
        return data

    def clean_motorcycle_parking_num(self):
        data = self.cleaned_data['motorcycle_parking_num']

        if data < 0:
            raise ValidationError(_('Motorcycle parking spaces cannot be less than 0'))
        # Remember to always return the cleaned data.
        return data

    def clean_bicycle_parking_num(self):
        data = self.cleaned_data['bicycle_parking_num']

        if data < 0:
            raise ValidationError(_('Bicycle parking spaces cannot be less than 0'))
        # Remember to always return the cleaned data.
        return data

    def clean_visit_car_parking_num(self):
        data = self.cleaned_data['visit_car_parking_num']

        if data < 0:
            raise ValidationError(_('Visitor car parking spaces cannot be less than 0'))
        # Remember to always return the cleaned data.
        return data

    def clean_visit_motorcycle_parking_num(self):
        data = self.cleaned_data['visit_motorcycle_parking_num']

        if data < 0:
            raise ValidationError(_('Visitor motorcycle parking spaces cannot be less than 0'))
        # Remember to always return the cleaned data.
        return data

    def clean_visit_bicycle_parking_num(self):
        data = self.cleaned_data['visit_bicycle_parking_num']

        if data < 0:
            raise ValidationError(_('Visitor bicycle parking spaces cannot be less than 0'))
        # Remember to always return the cleaned data.
        return data

    def clean_grace_time(self):
        data = self.cleaned_data['grace_time']

        if data < 0:
            raise ValidationError(_('Grace time cannot be less than 0'))
        # Remember to always return the cleaned data.
        return data

    def clean_car_payment_value(self):
        data = self.cleaned_data['car_payment_value']

        if data < 0:
            raise ValidationError(_('Car payment value cannot be less than 0'))
        # Remember to always return the cleaned data.
        return data

    def clean_motorcycle_payment_value(self):
        data = self.cleaned_data['motorcycle_payment_value']

        if data < 0:
            raise ValidationError(_('Motorcycle payment value cannot be less than 0'))
        # Remember to always return the cleaned data.
        return data

    def clean_bicycle_payment_value(self):
        data = self.cleaned_data['bicycle_payment_value']

        if data < 0:
            raise ValidationError(_('Bicycle payment value cannot be less than 0'))
        # Remember to always return the cleaned data.
        return data


class ModConfigurationForm(ModelForm):
    class Meta:
        model = Configuration
        exclude = ['co_ownership', ]

    def __init__(self, *args, **kwargs):
        super(ModConfigurationForm, self).__init__(*args, **kwargs)

    def clean_max_weight(self):
        data = self.cleaned_data['max_weight']

        if data < 0:
            raise ValidationError(_('Max weight cannot be less than 0'))
        # Remember to always return the cleaned data.
        return data

    def clean_max_axis(self):
        data = self.cleaned_data['max_axis']

        if data < 0:
            raise ValidationError(_('Max axis cannot be less than 0'))
        if data > 10:
            raise ValidationError(_('Max axis cannot be greater than 10'))
        # Remember to always return the cleaned data.
        return data

    def clean_car_parking_num(self):
        data = self.cleaned_data['car_parking_num']

        if data < 0:
            raise ValidationError(_('Car parking spaces cannot be less than 0'))
        # Remember to always return the cleaned data.
        return data

    def clean_motorcycle_parking_num(self):
        data = self.cleaned_data['motorcycle_parking_num']

        if data < 0:
            raise ValidationError(_('Motorcycle parking spaces cannot be less than 0'))
        # Remember to always return the cleaned data.
        return data

    def clean_bicycle_parking_num(self):
        data = self.cleaned_data['bicycle_parking_num']

        if data < 0:
            raise ValidationError(_('Bicycle parking spaces cannot be less than 0'))
        # Remember to always return the cleaned data.
        return data

    def clean_visit_car_parking_num(self):
        data = self.cleaned_data['visit_car_parking_num']

        if data < 0:
            raise ValidationError(_('Visitor car parking spaces cannot be less than 0'))
        # Remember to always return the cleaned data.
        return data

    def clean_visit_motorcycle_parking_num(self):
        data = self.cleaned_data['visit_motorcycle_parking_num']

        if data < 0:
            raise ValidationError(_('Visitor motorcycle parking spaces cannot be less than 0'))
        # Remember to always return the cleaned data.
        return data

    def clean_visit_bicycle_parking_num(self):
        data = self.cleaned_data['visit_bicycle_parking_num']

        if data < 0:
            raise ValidationError(_('Visitor bicycle parking spaces cannot be less than 0'))
        # Remember to always return the cleaned data.
        return data

    def clean_grace_time(self):
        data = self.cleaned_data['grace_time']

        if data < 0:
            raise ValidationError(_('Grace time cannot be less than 0'))
        # Remember to always return the cleaned data.
        return data

    def clean_car_payment_value(self):
        data = self.cleaned_data['car_payment_value']

        if data < 0:
            raise ValidationError(_('Car payment value cannot be less than 0'))
        # Remember to always return the cleaned data.
        return data

    def clean_motorcycle_payment_value(self):
        data = self.cleaned_data['motorcycle_payment_value']

        if data < 0:
            raise ValidationError(_('Motorcycle payment value cannot be less than 0'))
        # Remember to always return the cleaned data.
        return data

    def clean_bicycle_payment_value(self):
        data = self.cleaned_data['bicycle_payment_value']

        if data < 0:
            raise ValidationError(_('Bicycle payment value cannot be less than 0'))
        # Remember to always return the cleaned data.
        return data


class CreateApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        exclude = ['co_ownership', ]


class CreateParkingPlaceForm(ModelForm):
    class Meta:
        model = ParkingPlace
        exclude = ['co_ownership', ]

    def clean_area(self):
        data = self.cleaned_data['area']

        if data <= 0:
            raise ValidationError(_('Area cannot be less than or equal to 0'))

        # Remember to always return the cleaned data.
        return data

    def clean_admitted_weight(self):
        data = self.cleaned_data['admitted_weight']

        if data < 0:
            raise ValidationError(_('Admitted weight cannot be less than 0'))

        # Remember to always return the cleaned data.
        return data

    def clean_admitted_axis(self):
        data = self.cleaned_data['admitted_axis']

        if data < 0:
            raise ValidationError(_('Admitted axis cannot be less than 0'))

        # Remember to always return the cleaned data.
        return data


class InhabitantVehicleForm(ModelForm):
    class Meta:
        model = InhabitantVehicle
        fields = ['parking_place', 'owner', 'brand', 'model', 'color', 'type', 'weight', 'axis', 'plate', 'picture',
                  'property_letter', 'soat', 'due_date']

    def __init__(self, *args, **kwargs):
        co_ownership_id = kwargs.pop("co_ownership_id", None)
        super(InhabitantVehicleForm, self).__init__(*args, **kwargs)
        if co_ownership_id:
            co_ownership = get_object_or_404(CoOwnership, id=co_ownership_id)
            self.fields['owner'].queryset = Inhabitant.objects.filter(apartment__co_ownership=co_ownership)

    def clean_due_date(self):
        data = self.cleaned_data['due_date']

        # Check date is not in past.
        if data <= datetime.date.today():
            raise ValidationError(_('Due date cannot be less than or equal to today'))
        # Check date is in range allowed (+4 weeks)
        if data < datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(
                _('Due date cannot be less than 4 weeks'))

        # Remember to always return the cleaned data.
        return data

    def clean_weight(self):
        data = self.cleaned_data['weight']

        if data <= 0:
            raise ValidationError(_('Weight cannot be less than or equal to 0'))

        # Remember to always return the cleaned data.
        return data

    def clean_axis(self):
        data = self.cleaned_data['axis']

        if data <= 0:
            raise ValidationError(_('Axis cannot be less than or equal to 0'))
        # Check date is not in past.
        if data > 10:
            raise ValidationError(_('Axis cannot be greater than 10'))

        # Remember to always return the cleaned data.
        return data


class InhabitantPaymentForm(ModelForm):
    class Meta:
        model = InhabitantPayments
        fields = ['inhabitant', 'payment_date']

    def __init__(self, *args, **kwargs):
        co_ownership_id = kwargs.pop("co_ownership_id", None)
        super(InhabitantPaymentForm, self).__init__(*args, **kwargs)
        if co_ownership_id:
            co_ownership = get_object_or_404(CoOwnership, id=co_ownership_id)
            self.fields['inhabitant'].queryset = Inhabitant.objects.filter(apartment__co_ownership=co_ownership)


class SecurityGuardForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='First name')
    last_name = forms.CharField(max_length=100, help_text='Last name')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', ]
