# -*- coding: utf-8 -*-
from django import forms
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['profile_picture',]