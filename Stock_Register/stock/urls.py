from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    # path('login/',views.login_user,name="login"),
    # path('logout/',views.logout_user,name="logout"),
    path('add-stocks/',views.add_stocks,name="add_stocks"),
    path('selling-product/',views.selling_product,name="selling_product"),
    path('stock-details/',views.stock_details,name="stock_details"),
    path('payments/',views.payments,name="payments"),
    path('payment-details/',views.payment_details,name="payment_details"),
    path('get-product-price/',views.get_product_price,name="get_product_price"),
    path('get-stock-details/',views.get_stock_details,name="get_stock_details"),
    path('get-stock-history/',views.get_stock_history,name="get_stock_history"),
    # path('export-to-excel/', views.export_to_excel, name='export_to_excel'),
    #path('download-data/<str:data_type>/', views.download_data, name='download_data'),
]
