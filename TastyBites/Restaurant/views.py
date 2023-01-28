import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from .models import Menu


def menu(request):
    dishes = Menu.objects.all()
    template = render_to_string('menu.html', {'menu': dishes, 'user': request.user})
    return HttpResponse(template)


@login_required(login_url='')
def shoppingCart(request):
    try:
        cookie = json.loads(request.COOKIES.get('orders'))
        orders = []
        for c in cookie:
            d = {'order': Menu.objects.get(pk=c['order']), 'sauce': c['sauce'], 'meat': c['meat']}
            orders.append(d)
    except Exception as e:
        orders = []

    template = render_to_string('cart.html', {'user': request.user, 'cart': orders})
    return HttpResponse(template)


@login_required(login_url='')
def orders(request):
    if request.user.is_superuser:
        template = render_to_string('orders.html')
        return HttpResponse(template)

    return redirect('/')
