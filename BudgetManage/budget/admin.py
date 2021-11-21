from django.contrib import admin
from budget.models import SavingMethod, Category

# Register your models here.
admin.site.register(SavingMethod)
admin.site.register(Category)