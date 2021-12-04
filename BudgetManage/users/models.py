from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models import Model, OneToOneField, CASCADE, TextField, ForeignKey


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    goal = TextField()

    def __str__(self):
        return self.user.username
