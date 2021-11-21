from django.db import models
from django.db.models import CharField,IntegerField, ForeignKey

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