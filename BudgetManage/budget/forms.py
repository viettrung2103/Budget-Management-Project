
from django.core.exceptions import ValidationError
from django.forms import(
    CharField, ModelForm,DateField,DecimalField
)
from budget.models import (SavingMethod, Category, SpendingType, Spending, Income,
)
from datetime import date,datetime

class MethodForm(ModelForm):

    class Meta:
        model = SavingMethod
        fields ='__all__'

    #Force the first letter of the name to be capitalized
    def clean_name(self):
        initial = self.cleaned_data['name']
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
        super().validate(value)
        if value > date.today():
            raise ValidationError("No Future dates allowed!")

    def clean(self,value):
        result = super().clean(value)
        return date(year=result.year,month=result.month,day=result.day)

class SpendingForm(ModelForm):
    class Meta:
        model = Spending
        fields = '__all__'

    date = PastandNowField()
    amount = DecimalField(min_value=0)

class IncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = '__all__'

    date = PastandNowField
    amount = DecimalField(min_value=0)



