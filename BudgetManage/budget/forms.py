
from django.core.exceptions import ValidationError
from django.forms import(
    CharField, ModelForm,DateField
)
from budget.models import SavingMethod, Category, SpendingType, Spending

from datetime import date

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

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    # Force the first letter of the name to be capitalized
    def clean_name(self):
        initial = self.cleaned_data['name']
        if initial == '':
            raise ValidationError("You cannot add empty method")
        return initial.capitalize()

class SpendingTypeForm(ModelForm):
    class Meta:
        model = SpendingType
        fields = '__all__'

    # Force the first letter of the name to be capitalized
    def clean_name(self):
        initial = self.cleaned_data['name']
        if initial == '':
            raise ValidationError("You cannot add empty method")
        return initial.capitalize()

class PastandNowField(DateField):
    def validate(self, value):
        initial = super().validate(value)
        if initial > date.xtoday():
            raise ValidationError("No Future dates allowed!")

    def clean(self,value):
        result = super().clean(value)
        return date(date=result.date,month=result.month,year=result.year)

class SpendingForm(ModelForm):
    class Meta:
        model = Spending
        fields = '__all__'

    date = PastandNowField()


