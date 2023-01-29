import datetime
import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import generic

from .forms import AddOrderForm, SignUpFormLabels
from .models import Menu, Order


def menu(request):
    dishes = Menu.objects.all()
    template = render_to_string('menu.html', {'menu': dishes, 'user': request.user})
    print(datetime.datetime.now())
    return HttpResponse(template)


@login_required(login_url='')
def shoppingCart(request):
    if not request.user.is_superuser:
        # Get orders for user
        cookie = []
        total = 0
        try:
            cookie = json.loads(request.COOKIES.get('orders'))
            orders = []
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

    return redirect('/')


@login_required(login_url='')
def orders(request):
    if request.user.is_superuser:
        template = render_to_string('orders.html')
        return HttpResponse(template)

    return redirect('/')


@login_required(login_url='')
def userpanel(request):
    ord = Order.objects.all()
    history = []
    for h in ord:
        if h.username == request.user:
            kebabs = ""
            for i in h.orders:
                kebabs += Menu.objects.get(pk=i['order']).dishName + " "
            history.append({'kebabs': kebabs, 'history': h, 'completed': h.completed})

    if request.method == 'POST':
        rem = User.objects.get(username=request.user)
        if rem is not None:
            rem.delete()
            return redirect('/')

    template = render(request, 'userpanel.html', {'user': request.user, 'history': history})
    return HttpResponse(template)


class SignUpView(generic.CreateView):
    form_class = SignUpFormLabels
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
