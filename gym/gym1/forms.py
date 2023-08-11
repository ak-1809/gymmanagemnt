from django import forms
from .models import Trainer,Subscriber,GymEquipment

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ( 'name','expertise','contact')


class MemberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('first_name', 'last_name', 'email', 'phone')


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = GymEquipment
        fields = ('name', 'manufacturer', 'quantity')
