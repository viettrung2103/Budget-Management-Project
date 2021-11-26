from django.db import models
from django.db.models import (CharField,IntegerField, ForeignKey, DecimalField, DateField,TextField,DateTimeField
)
import datetime
from django.forms.widgets import SelectDateWidget
# Create your models here.
class SavingMethod(models.Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = CharField(max_length=128)
    method = ForeignKey(SavingMethod, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class SpendingType(models.Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name

class Spending(models.Model):
    name = CharField(max_length=128)
    spendingtype = ForeignKey(SpendingType,null=True, on_delete=models.CASCADE)
    amount = DecimalField(max_digits=8,decimal_places=2)
    category = ForeignKey(Category, null=True,on_delete=models.DO_NOTHING)
    date = DateField(default=datetime.date.today)# date field , default is today
    description = TextField()

    def __str__(self):
        return self.name


