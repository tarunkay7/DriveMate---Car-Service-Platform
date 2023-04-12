# Generated by Django 4.1.7 on 2023-03-31 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drivemate", "0006_delete_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("category", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
