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
    template = render_to_string('cart.html')
    return HttpResponse(template)


@login_required(login_url='')
def orders(request):
    if request.user.is_superuser:
        template = render_to_string('orders.html')
        return HttpResponse(template)

    return redirect('/')
