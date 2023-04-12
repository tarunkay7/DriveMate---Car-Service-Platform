from django.contrib import admin

from drivemate.models import Car, Customer, Product,Services

# Register your models here.
admin.site.register(Car)
admin.site.register(Customer)
admin.site.register(Services)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price')
