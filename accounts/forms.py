from django.db.models.base import Model
from django.forms import forms, ModelForm
from django.forms import fields
from .models import User

class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'password']