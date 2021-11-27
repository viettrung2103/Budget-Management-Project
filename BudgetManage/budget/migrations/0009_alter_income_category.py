# Generated by Django 3.2.9 on 2021-11-27 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0008_income'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='category',
            field=models.CharField(choices=[('', 'Type of Income'), ('Salary', 'Salary'), ('Dividend', 'Dividend'), ('Extra', 'Extra'), ('Business', 'Business')], default=None, max_length=8),
        ),
    ]
