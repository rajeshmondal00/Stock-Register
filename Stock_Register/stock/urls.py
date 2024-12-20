from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('add-stocks/',views.add_stocks,name="add_stocks"),
    path('selling-product/',views.selling_product,name="selling_product"),
    path('stock-details/',views.stock_details,name="stock_details"),
]
