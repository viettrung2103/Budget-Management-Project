
from django.core.exceptions import ValidationError
from django.forms import(
    CharField, ModelForm
)
from budget.models import SavingMethod


class MethodForm(ModelForm):

    class Meta:
        model = SavingMethod
        fields ='__all__'

    #Force the first letter of the name to be capitalized
    def clean_name(self):
        initial = self.cleaned_data('name')
        if initial == '':
            raise ValidationError("You cannot add empty method")
        return initial.capitalize()
