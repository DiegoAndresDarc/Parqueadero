from django import forms
from django.forms import ModelForm

from security_guard.models import Visitor, VisitorVehicle


class GetParkingFromBarcodeForm(forms.Form):
    barcode = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(GetParkingFromBarcodeForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if isinstance(self.fields[field], forms.fields.CharField):
                self.fields[field].widget.attrs.update({'class': 'input'})


class GetVisitorFromIdentificationForm(forms.Form):
    identification = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super(GetVisitorFromIdentificationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'input'})


class CreateVisitorForm(ModelForm):
    class Meta:
        model = Visitor
        exclude = ['co_ownership', ]

    def __init__(self, *args, **kwargs):
        super(CreateVisitorForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if isinstance(self.fields[field], forms.fields.TypedChoiceField):
                self.fields[field].widget.attrs.update({'class': 'select'})
            else:
                self.fields[field].widget.attrs.update({'class': 'input'})


class CreateVisitorVehicleForm(ModelForm):
    class Meta:
        model = VisitorVehicle
        exclude = ['owner', 'parking_place', ]

    def __init__(self, *args, **kwargs):
        super(CreateVisitorVehicleForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if isinstance(self.fields[field], forms.fields.TypedChoiceField):
                self.fields[field].widget.attrs.update({'class': 'select'})
            elif isinstance(self.fields[field], forms.fields.ImageField):
                self.fields[field].widget.attrs.update({'class': 'file-label'})
            else:
                self.fields[field].widget.attrs.update({'class': 'input'})

