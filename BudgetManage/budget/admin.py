from django.contrib import admin
from budget.models import SavingMethod, Category, Spending, Income, Budget

# Register your models here.
admin.site.register(SavingMethod)
admin.site.register(Category)
admin.site.register(Spending)
admin.site.register(Income)
admin.site.register(Budget)
