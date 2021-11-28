from django.db import models
from django.db.models import (CharField,IntegerField,
                            OneToOneField, DecimalField
)
from budget.models import Category
# Create your models here.

class BudgetMethod(models.Model):
    name = CharField(max_length=128)

    def __str__(self):
        return  self.name

class Budget(models.Model):
    budget_type = OneToOneField(
        Category,
        on_delete=models.CASCADE,
) #HAVE A SAME CATEGORY WITH SPENDING CATEGORY
    amount = DecimalField(max_digits=8,decimal_places=2)
