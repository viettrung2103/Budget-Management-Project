import re

from django.forms import(
    CharField, ModelForm

from models import Method


class MethodForm(ModelForm):

    class Meta:
        model = Method
        fiels ='__all__'

    #Force the first letter of the name to be capitalized
    def clean_name(self):
        initial = self.cleaned_data('name')
        return initial.capitalize()
