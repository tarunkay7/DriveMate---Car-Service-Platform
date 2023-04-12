from datetime import datetime, timedelta
from random import randint
from twilio.rest import Client

from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404

from Drivemate import settings
from .forms import CustomerForm
from .cart import Cart
from .models import Services, Customer


# Create your views here.

def send_sms(phone_number,message):
    account_sid = 'ACf8419a76b00ddbfcae70e6c88970cb96'
    auth_token = '35ce0717f0910bc738db7a34670448d9'

    from_phone_number = '+15673863526'

    to_phone_number = '+91' + str(phone_number)

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_=from_phone_number,
        to=to_phone_number
    )

    print(f'Sent SMS to {to_phone_number}. Message ID: {message.sid}')


def home(request):
    return render(request, 'home.html')


def logout(request):
    clear_cart(request)
    request.session.clear()
    return redirect('home')


def login_view(request):
    if request.method == 'POST':
        phone_number = request.POST['phone']
        password = request.POST['password']

        try:
            customer = Customer.objects.get(phone=phone_number, password=password)
        except Customer.DoesNotExist:
            return redirect('login_view')

        request.session['customer_id'] = customer.id
        request.session['customer_name'] = customer.name
        return redirect('dashboard')

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CustomerForm()
    return render(request, 'signup.html', {'form': form})


def session_exists(request):
    if request.session.get('customer_id'):
        return True
    else:
        return False


def dashboard(request):
    if session_exists(request):
        customer_name = request.session.get('customer_name')
        cart_items = Cart(request).get_total_items()
        context = {
            'customer_name': customer_name,
            'cart_items': cart_items
        }
        return render(request, 'dashboard.html', {'item': context})
    else:
        return render(request, 'login.html')


def acservices(request):
    if session_exists(request):
        ac_services = Services.objects.filter(category='AC')
        context = {
            'ac_services': ac_services
        }
        return render(request, 'acservice.html', context)


def detailing(request):
    if session_exists(request):
        ac_services = Services.objects.filter(category='Detailing')
        context = {
            'detailing_services': ac_services
        }
        return render(request, 'detailing.html', context)


def battery_services(request):
    if session_exists(request):
        battery_products = Services.objects.filter(category='Battery')
        cart_items = Cart(request).get_total_items()
        context = {
            'battery_products': battery_products,
            'cart_items': cart_items
        }
        return render(request, 'battery_services.html', {'item': context})


def add_to_cart(request, product_name):
    cart = Cart(request)
    cart.add(product_name)
    print("product is added")
    return redirect('cart')


def remove_from_cart(request, item_name):
    cart = Cart(request)
    cart.remove(item_name)
    messages.success(request, f'{item_name} removed from cart.')
    return redirect('cart')


def cart(request):
    if session_exists(request):
        cart = Cart(request)
        items = cart.get_items()
        num_items = cart.get_total_items()
        total_price = cart.get_total_price()
        print(num_items)
        for item in items:
            item['item_price'] = float(item['price']) * int(item['quantity'])

        context = {
            'items': items,
            'total_price': total_price,
            'num_items': num_items
        }
        return render(request, 'cart.html', context)


def clear_cart(request):
    request.session[settings.CART_SESSION_ID] = {}
    return redirect('cart')


def increase_item_quantity(request, item_name):
    cart = Cart(request)
    cart.add(item_name, quantity=1)
    messages.success(request, f'{item_name} quantity increased.')
    return redirect('cart')


def decrease_item_quantity(request, item_name):
    cart = Cart(request)
    cart.add(item_name, quantity=-1)
    messages.success(request, f'{item_name} quantity decreased.')
    return redirect('cart')


def checkout(request):
    if session_exists(request):
        cart = Cart(request)
        items = cart.get_items()
        total_price = cart.get_total_price()
        for item in items:
            item['item_price'] = float(item['price']) * int(item['quantity'])

        context = {
            'items': items,
            'total_price': total_price
        }

        return render(request, 'checkout.html', context)


def suffix(d):
    return "th" if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')


def payment_success(request):
    if session_exists(request):
        customer_id = request.session.get('customer_id')
        customer = Customer.objects.get(id=customer_id)
        phone_number = customer.phone
        current_date = datetime.now().date()
        delivery_date = current_date + timedelta(days=randint(1, 3))
        phone_message = "Your order has been placed.Our executive will reach you by " + delivery_date.strftime("%d %B %Y").replace("{0}", str(delivery_date.day) + suffix(
                delivery_date.day))

        context = {
            'message': 'Order Placed Successfully',
            'delivery_date': delivery_date.strftime("%d %B %Y").replace("{0}", str(delivery_date.day) + suffix(
                delivery_date.day))
        }
        send_sms(phone_number,phone_message)
        return render(request, 'payment_success.html', context)


def get_num_item_cart(request):
    cart = Cart(request)
    return cart.get_total_items()
