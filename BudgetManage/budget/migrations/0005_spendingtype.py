# Generated by Django 3.2.9 on 2021-11-21 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0004_category_method'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpendingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
    ]
