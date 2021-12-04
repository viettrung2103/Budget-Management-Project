from django.db import models
from django.db.models import (CharField,IntegerField, ForeignKey, DecimalField, DateField,TextField,
                              DateTimeField,TextChoices
)
import datetime
from users.models import Profile
from django.forms.widgets import SelectDateWidget
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Record(models.Model):
    name = CharField(max_length=128, null=True)
    user = ForeignKey(Profile,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SavingMethod(models.Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = CharField(max_length=128)
    method = ForeignKey(SavingMethod, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class Spending(models.Model):
    name = CharField(max_length=128)
    amount = DecimalField(max_digits=8,decimal_places=2)
    category = ForeignKey(Category,related_name='spendings', null=True,on_delete=models.DO_NOTHING)
    date = DateField(default=datetime.date.today)# date field , default is today
    description = TextField()
    record = ForeignKey(Record,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

class Income(models.Model):

    class IncomeType(models.TextChoices):
        NONE = '',_('Type of Income')
        SALARY = 'Salary',_('Salary')
        DIVIDEND = 'Dividend',_('Dividend')
        EXTRA = 'Extra',_('Extra')
        BUSINESS = 'Business',_('Business')

    name = CharField(max_length=128)
    amount = DecimalField(max_digits=8,decimal_places=2)
    category = CharField(
        max_length=8,
        choices=IncomeType.choices,
        default=None,
    )
    date = DateField(default=datetime.date.today)# date field , default is today
    description = TextField()
    record = ForeignKey(Record, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


