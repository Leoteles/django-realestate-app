# Generated by Django 5.0.2 on 2024-03-18 15:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0002_alter_contact_contact_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="contact_date",
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
