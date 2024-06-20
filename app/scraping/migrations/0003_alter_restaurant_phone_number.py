# Generated by Django 5.0.6 on 2024-06-20 12:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scraping", "0002_restaurant_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="restaurant",
            name="phone_number",
            field=models.CharField(
                max_length=16,
                validators=[
                    django.core.validators.RegexValidator(
                        regex="^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$"
                    )
                ],
            ),
        ),
    ]