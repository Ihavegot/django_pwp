from django.urls import path
from django.views.generic import TemplateView

from . import views
from .views import SignUpView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('menu/', views.menu),
    path('cart/', views.shoppingCart),
    path('orders/', views.orders),
    path('userpanel/', views.userpanel),
    path("signup/", SignUpView.as_view(), name="signup")
]
