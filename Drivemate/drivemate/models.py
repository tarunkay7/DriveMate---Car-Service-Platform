from django.db import models


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Services(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, default=None, null=True)




