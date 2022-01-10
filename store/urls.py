from django.urls import path

from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("", cache_page(60)(views.store), name="store"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("update_item/", views.updateItem, name="update_item"),
    path("process_order/", views.processOrder, name="process_order"),
    path("addpage/", views.addpage, name="addpage"),
    path("contacts/", cache_page(60)(views.contacts), name="contacts"),
]
