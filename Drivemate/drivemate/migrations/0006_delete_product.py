# Generated by Django 4.1.7 on 2023-03-31 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("drivemate", "0005_remove_product_customer"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Product",
        ),
    ]