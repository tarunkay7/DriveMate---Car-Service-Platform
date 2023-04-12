from decimal import Decimal
from django.conf import settings
from django.core.serializers import json

from drivemate.models import Product, Services


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product_name, quantity=1):
        products = Services.objects.filter(name=product_name)
        if not products:
            # product not found
            return False
        product = products[0]
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price),
                                     'name': product.name,
                                     'category': product.category}
        new_quantity = self.cart[product_id]['quantity'] + quantity
        if new_quantity < 1:
            # minimum quantity is 1
            new_quantity = 1
        elif new_quantity > 10:
            # maximum quantity is 10
            new_quantity = 10
        self.cart[product_id]['quantity'] = new_quantity

        self.save()
        return True

    def get_items(self):
        product_ids = self.cart.keys()
        products = Services.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        return self.cart.values()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True


    def __iter__(self):
        product_ids = self.cart.keys()
        products = Services.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['name'] = product.name
            self.cart[str(product.id)]['category'] = product.category
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def remove(self, item_name):
        for item_id, item in self.cart.items():
            if item['name'] == item_name:
                del self.cart[item_id]
                self.save()
                break
    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    def get_total_items(self):
        return sum(item['quantity'] for item in self.cart.values())
