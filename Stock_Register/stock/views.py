from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse,JsonResponse
from .models import *
import csv

## home page
def home(request):
    return render(request,"index.html")

## add products to the stock 
def add_stocks(request):
    products = Product.objects.all() # filter the product details
    suppliers = Supplier.objects.all() # filter the supplier details
    return render(request,"add_stock.html",{"product":products,"suppliers":suppliers})

## sell products from the stock
def selling_product(request): 
    products = Product.objects.all() # filter the product details
    return render(request,"sell_products.html",{"product":products})

## view current details of the stock
def stock_details(request):
    return render(request,"stock_details.html")


def payments(request):
    return render(request,"payments.html")

## view the payment details
def payment_details(request):
    return render(request,"payment_details.html")



def export_to_excel(request):
    data = YourModel.objects.all().values()
    df = pd.DataFrame(list(data))

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="exported_data.xlsx"'
    df.to_excel(response, index=False, engine='openpyxl')
    return response

def view_stock(request):
    # Fetch current stock data
    current_stock = Product.objects.all()

    # Fetch stock history
    stock_history = StockTransaction.objects.select_related('product').order_by('-date')

    return render(request, 'view_stock.html', {
        'current_stock': current_stock,
        'stock_history': stock_history,
    })

def download_data(request, data_type):
    # Create CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{data_type}_data.csv"'

    writer = csv.writer(response)

    if data_type == 'product':
        products = Product.objects.all()
        writer.writerow(['Product Name', 'Category', 'Description', 'Price per Unit', 'Quantity'])
        for product in products:
            writer.writerow([product.name, product.category, product.description, product.price_per_unit, product.quantity])

    elif data_type == 'sell':
        transactions = StockTransaction.objects.filter(transaction_type='sell').select_related('product')
        writer.writerow(['Date', 'Product Name', 'Quantity', 'Total Price'])
        for txn in transactions:
            writer.writerow([txn.date, txn.product.name, txn.quantity, txn.quantity * txn.product.price_per_unit])

    elif data_type == 'current':
        products = Product.objects.all()
        writer.writerow(['Product Name', 'Quantity'])
        for product in products:
            writer.writerow([product.name, product.quantity])

    else:
        return JsonResponse({'error': 'Invalid data type'}, status=400)

    return response