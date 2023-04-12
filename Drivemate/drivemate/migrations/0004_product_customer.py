# Generated by Django 4.1.7 on 2023-03-31 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("drivemate", "0003_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="customer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="drivemate.customer",
            ),
        ),
    ]
