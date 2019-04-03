from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Database


class Customusercreationform(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model=Database
        fields=UserCreationForm.Meta.fields


class Customuserchangeform(UserChangeForm):
    class Meta:
        model=Database
        fields=UserChangeForm.Meta.fields