from django.urls import path
from django.views.generic import TemplateView, ListView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('menu/', views.menu),
    path('cart/', views.shoppingCart),
    path('orders/', views.orders),
]
