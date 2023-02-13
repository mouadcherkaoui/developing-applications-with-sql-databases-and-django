from dataclasses import fields
from socket import fromshare
from typing import no_type_check_decorator
from django import forms
from .models import Course

class Courseform(forms.ModelForm):
    """"Form for new course"""
    @no_type_check_decorator()
    class Meta:
        model: Course
        fields: ('name', 'image', 'description')