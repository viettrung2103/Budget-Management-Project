from django.db import models
from django.db.models import CharField

# Create your models here.
class SavingMethod(models.Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name