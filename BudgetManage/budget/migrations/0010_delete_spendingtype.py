# Generated by Django 3.2.9 on 2021-11-27 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0009_alter_income_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SpendingType',
        ),
    ]