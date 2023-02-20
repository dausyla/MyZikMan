from django import forms
from user.models import User,Band
from django.forms import fields

class UserForm(forms.ModelForm):
    class Meta:
        # get the User model
        model = User
        fields = "__all__"

class BandForm(forms.ModelForm):
    class Meta:
        # get the Band model
        model = Band
        fields = "__all__"
