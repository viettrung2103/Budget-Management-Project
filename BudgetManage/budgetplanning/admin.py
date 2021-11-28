from django.contrib import admin

from budgetplanning.models import BudgetMethod, Budget

# Register your models here.
admin.site.register(BudgetMethod)
admin.site.register(Budget)
