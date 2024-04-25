from django import forms
from django.forms import ModelForm

from security_guard.models import Visitor, VisitorVehicle


class GetParkingFromBarcodeForm(forms.Form):
    barcode = forms.CharField(widget=forms.PasswordInput)


class GetVisitorFromIdentificationForm(forms.Form):
    identification = forms.IntegerField()


class CreateVisitorForm(ModelForm):
    class Meta:
        model = Visitor
        exclude = ['co_ownership', ]


class CreateVisitorVehicleForm(ModelForm):
    class Meta:
        model = VisitorVehicle
        exclude = ['owner', 'parking_place', ]

