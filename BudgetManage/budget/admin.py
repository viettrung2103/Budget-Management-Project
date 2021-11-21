from django.contrib import admin
from budget.models import SavingMethod, Category, SpendingType, Spending

# Register your models here.
admin.site.register(SavingMethod)
admin.site.register(Category)
admin.site.register(SpendingType)
admin.site.register(Spending)
