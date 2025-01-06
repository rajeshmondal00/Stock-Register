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
    # path('export-to-excel/', views.export_to_excel, name='export_to_excel'),
    # path('add-stock/', views.add_stock_view, name='add_stock'),
    # path('get-products/', views.get_products, name='get_products'),
    #path('view-stock/', views.view_stock, name='view_stock'),
    #path('download-data/<str:data_type>/', views.download_data, name='download_data'),
]
