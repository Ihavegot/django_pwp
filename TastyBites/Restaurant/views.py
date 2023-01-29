import datetime
import json

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from .forms import AddOrderForm
from .models import Menu, Order


def set_cookie(response, key, value, days_expire=7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
        "%a, %d-%b-%Y %H:%M:%S GMT",
    )
    response.set_cookie(
        key,
        value,
        path='/',
        max_age=max_age,
        expires=expires,
        domain=settings.SESSION_COOKIE_DOMAIN,
        secure=settings.SESSION_COOKIE_SECURE or None,
    )


def menu(request):
    dishes = Menu.objects.all()
    template = render_to_string('menu.html', {'menu': dishes, 'user': request.user})
    print(datetime.datetime.now())
    return HttpResponse(template)


@login_required(login_url='')
def shoppingCart(request):
    # Get orders for user
    cookie = []
    try:
        cookie = json.loads(request.COOKIES.get('orders'))
        orders = []
        total = 0
        for c in cookie:
            temp = Menu.objects.get(pk=c['order'])
            d = {'order': temp, 'sauce': c['sauce'], 'meat': c['meat']}
            orders.append(d)
            total += int(temp.dishPrice)
    except Exception as e:
        print(e)
        orders = []

    # Add orders
    saved = False
    if request.method == "POST":
        form = AddOrderForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            adres = form.cleaned_data['adres']
            info = form.cleaned_data['info']
            newOrder = Order(username=request.user, orders=cookie, phone=phone,
                             adres=adres, info=info)
            newOrder.save()
            orders = []
            saved = True
    else:
        form = AddOrderForm()

    allOrders = Order.objects.all()
    template = render(request, 'cart.html',
                      {'user': request.user, 'cart': orders, 'form': form, 'ord': allOrders, 'total': total})
    response = HttpResponse(template)
    if saved:
        response.set_cookie('orders', path='/')
    return response


@login_required(login_url='')
def orders(request):
    if request.user.is_superuser:
        template = render_to_string('orders.html')
        return HttpResponse(template)

    return redirect('/')
