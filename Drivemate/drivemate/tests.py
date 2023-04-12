from django.test import TestCase

# Create your tests here.
from .models import Car

car_names = ['Maruti Suzuki Swift', 'Hyundai Creta', 'Mahindra Thar', 'Tata Altroz', 'Kia Seltos', 'Renault Kwid',
             'Honda City', 'Toyota Fortuner', 'MG Hector', 'Volkswagen Polo']

for name in car_names:
    car = Car(name=name)
    car.save()
