from budgetplanning.models import BudgetMethod

class BudgetMethod(ModelForm):

    class Meta:
        model = BudgetMethod
        fields ='__all__'

    #Force the first letter of the name to be capitalized
    def clean_name(self):
        initial = self.cleaned_data['name']
        if initial == '':
            raise ValidationError("You cannot add empty method")
        return initial.capitalize()