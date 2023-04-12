# Generated by Django 4.1.7 on 2023-04-01 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drivemate", "0008_alter_product_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Services",
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
        migrations.AlterField(
            model_name="product",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
