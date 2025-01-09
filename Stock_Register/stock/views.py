from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse,JsonResponse
from .models import *
import csv,json
## home page
def home(request):
    return render(request,"index.html")

## add products to the stock 
def add_stocks(request):
    if request.method == "POST":
            buyer_name = request.POST.get("buyerName", "").strip()
            custom_buyer_name = request.POST.get("customBuyerName", "").strip()
            product_name = request.POST.get("productName", "").strip()
            custom_product_name = request.POST.get("customProductName", "").strip()
            date = request.POST.get("date", "")
            quantity = int(request.POST.get("quantity", 0))
            weight = int(request.POST.get("Weight", 0))
            payment_method = request.POST.get("paymentMethod", "").strip()
            price = int(request.POST.get("price", 0))

            # Additional Data from JavaScript
            supplier_id = request.POST.get("supplier_id", "").strip()
            product_id = request.POST.get("product_id", "").strip()

            Buy_Product.objects.create(
                supp_id=supplier_id,
                pro_id=product_id,
                buy_quantity=quantity,
                buy_date=date)
            # Process data
            print("quantity:",quantity)
            print("Supplier ID:", supplier_id)
            print("Product Name:", product_name)
            print("Product ID:", product_id)
            return JsonResponse({'success': True, 'message': 'Stock added successfully.'}, status=200)
        # except Product.DoesNotExist:
        #     return JsonResponse({'success': False, 'message': 'Product not found.'})
        # except Exception as e:
        #     return JsonResponse({'success': False, 'message': f'Error: {str(e)}'})

    products = Product.objects.all() # filter the product details
    suppliers = Supplier.objects.all() # filter the supplier details
    return render(request,"add_stock.html",{"products":products,"suppliers":suppliers})

## sell products from the stock
def selling_product(request): 
    if request.method == "POST":
        product_id = request.POST.get("product_id", "").strip()
        print(product_id)
        return JsonResponse({'success': True, 'message': 'Stock added successfully.'}, status=200)
    products = Product.objects.all() # filter the product details
    return render(request,"sell_products.html",{"products":products})

## view current details of the stock
def stock_details(request):
    products = Product.objects.all()
    return render(request,"stock_details.html",{"products":products})


def payments(request):
    suppliers = Supplier.objects.all() # filter the supplier details
    return render(request,"payments.html",{"suppliers":suppliers})

## view the payment details
def payment_details(request):
    return render(request,"payment_details.html")

def get_product_price(request):
    product_id = request.GET.get('product_id')
    if not product_id:
        return JsonResponse({'error': 'Product ID is required'}, status=400)

    try:
        product = Product.objects.get(pro_id=product_id)
        return JsonResponse({
            'product_id': product.pro_id,
            'product_name': product.pro_name,
            'price': product.pro_price,
            'weight': product.weight
        })
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

def get_stock_details(request):
    product_id = request.GET.get('product_id')
    if not product_id:
        return JsonResponse({'error': 'Product ID is required'}, status=400)

    try:
        # stock = Stock.objects.get(pro_id=product_id)
        product = Product.objects.get(pro_id=product_id)
        return JsonResponse({
            'product_id': product.pro_id,
            'product_name': product.pro_name,
            'quantity': 100,
            'price': product.pro_price,
            'weight': product.weight
        })
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404) 
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
