from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse,JsonResponse
from .models import *
import csv,json
from datetime import datetime
from .utility import *
## home page
def home(request):
    return render(request,"index.html")

## add products to the stock 
def add_stocks(request):
    if request.method == "POST":
            try:
                date = request.POST.get("date", "")
                quantity = request.POST.get("quantity")
                payment_method = request.POST.get("paymentMethod", "").strip()
                payment_value = request.POST.get("paymentValue")
                custome_buyer_name = request.POST.get("customBuyerName","").strip()
                custome_pro_name = request.POST.get("customProductName","").strip()
                supplier_id = request.POST.get("supplier_id", "").strip()
                product_id = request.POST.get("product_id", "").strip()
                weight = request.POST.get("Weight")
                price = request.POST.get("price")
                if custome_buyer_name != None and custome_pro_name != None:
                    auto_buyer_id = id_generator()
                    auto_pro_id = id_generator()
                    Supplier.objects.create(supp_id=auto_buyer_id,supp_name=custome_buyer_name)
                    Product.objects.create(pro_id=auto_pro_id,pro_name=custome_pro_name,crt_quantity=0,pro_price=price,weight=weight)
                    if payment_method == "cash" or payment_method == "online":
                        supplier=Supplier.objects.get(supp_id=auto_buyer_id)
                        product=Product.objects.get(pro_id=auto_pro_id)
                        auto_pay_id=id_generator()
                        Payment.objects.create(pay_id=auto_pay_id,supp_id=supplier,type=payment_method,amount=int(payment_value),pay_date=date)
                        payment = Payment.objects.get(pay_id=auto_pay_id)
                        cash_auto_buy_id=id_generator()
                        Buy_Product.objects.create(
                            buy_id=cash_auto_buy_id,
                            supp_id=supplier,
                            pro_id=product,
                            buy_quantity=int(quantity),
                            buy_date=date,
                            pay_id=payment)
                        buy_product=Buy_Product.objects.get(buy_id=cash_auto_buy_id)
                        Stock.objects.create(
                            buy_id=buy_product,
                            sto_id=id_generator(),
                            pro_id=product,
                            type="Buy",
                            quantity=buy_product.buy_quantity,
                            date=buy_product.buy_date,
                            price=int(quantity)*product.pro_price
                        )
                        product.crt_quantity += int(quantity)
                        product.save()
                    else:
                        supplier=Supplier.objects.get(supp_id=auto_buyer_id)
                        product=Product.objects.get(pro_id=auto_pro_id)
                        auto_buy_id=id_generator()
                        Buy_Product.objects.create(
                            buy_id=auto_buy_id,
                            supp_id=supplier,
                            pro_id=product,
                            buy_quantity=quantity,
                            buy_date=date)
                        buy_product=Buy_Product.objects.get(buy_id=auto_buy_id)
                        Stock.objects.create(
                            buy_id=buy_product,
                            sto_id=id_generator(),
                            pro_id=buy_product.pro_id,
                            type='Buy',
                            date=buy_product.buy_date,
                            quantity=buy_product.buy_quantity,
                            price=int(quantity)*product.pro_price
                        )
                        product.crt_quantity += int(quantity)
                        product.save()
                elif custome_pro_name != None:
                    auto_pro_id = id_generator()
                    Product.objects.create(pro_id=auto_pro_id,pro_name=custome_pro_name,crt_quantity=0,pro_price=price,weight=weight)
                    if payment_method == "cash" or payment_method == "online":
                        supplier=Supplier.objects.get(supp_id=supplier_id)
                        product=Product.objects.get(pro_id=auto_pro_id)
                        auto_pay_id=id_generator()
                        Payment.objects.create(pay_id=auto_pay_id,supp_id=supplier,type=payment_method,amount=int(payment_value),pay_date=date)
                        payment = Payment.objects.get(pay_id=auto_pay_id)
                        cash_auto_buy_id=id_generator()
                        Buy_Product.objects.create(
                            buy_id=cash_auto_buy_id,
                            supp_id=supplier,
                            pro_id=product,
                            buy_quantity=int(quantity),
                            buy_date=date,
                            pay_id=payment)
                        buy_product=Buy_Product.objects.get(buy_id=cash_auto_buy_id)
                        Stock.objects.create(
                            buy_id=buy_product,
                            sto_id=id_generator(),
                            pro_id=product,
                            type="Buy",
                            quantity=buy_product.buy_quantity,
                            date=buy_product.buy_date,
                            price=int(quantity)*product.pro_price
                        )
                        product.crt_quantity += int(quantity)
                        product.save()
                    else:
                        supplier=Supplier.objects.get(supp_id=supplier_id)
                        product=Product.objects.get(pro_id=auto_pro_id)
                        auto_buy_id=id_generator()
                        Buy_Product.objects.create(
                            buy_id=auto_buy_id,
                            supp_id=supplier,
                            pro_id=product,
                            buy_quantity=quantity,
                            buy_date=date)
                        buy_product=Buy_Product.objects.get(buy_id=auto_buy_id)
                        Stock.objects.create(
                            buy_id=buy_product,
                            sto_id=id_generator(),
                            pro_id=buy_product.pro_id,
                            type='Buy',
                            date=buy_product.buy_date,
                            quantity=buy_product.buy_quantity,
                            price=int(quantity)*product.pro_price
                        )
                        product.crt_quantity += int(quantity)
                        product.save()
                else:
                    if payment_method == "cash" or payment_method == "online":
                        supplier=Supplier.objects.get(supp_id=supplier_id)
                        product=Product.objects.get(pro_id=product_id)
                        auto_pay_id=id_generator()
                        Payment.objects.create(
                            pay_id=auto_pay_id,
                            supp_id=supplier,
                            type=payment_method,
                            amount=int(payment_value),
                            pay_date=date
                        )
                        payment = Payment.objects.get(pay_id=auto_pay_id)
                        cash_auto_buy_id=id_generator()
                        Buy_Product.objects.create(
                            buy_id=cash_auto_buy_id,
                            supp_id=supplier,
                            pro_id=product,
                            buy_quantity=int(quantity),
                            buy_date=date,
                            pay_id=payment)

                        buy_product=Buy_Product.objects.get(buy_id=cash_auto_buy_id)
                        Stock.objects.create(
                            buy_id=buy_product,
                            sto_id=id_generator(),
                            pro_id=product,
                            type="Buy",
                            quantity=buy_product.buy_quantity,
                            date=buy_product.buy_date,
                            price=int(quantity)*product.pro_price
                        )
                        product.crt_quantity += int(quantity)
                        product.save()
                    else:
                        supplier=Supplier.objects.get(supp_id=supplier_id)
                        product=Product.objects.get(pro_id=product_id)
                        auto_buy_id=id_generator()
                        Buy_Product.objects.create(
                            buy_id=auto_buy_id,
                            supp_id=supplier,
                            pro_id=product,
                            buy_quantity=quantity,
                            buy_date=date)
                        buy_product=Buy_Product.objects.get(buy_id=auto_buy_id)
                        Stock.objects.create(
                            buy_id=buy_product,
                            sto_id=id_generator(),
                            pro_id=buy_product.pro_id,
                            type='Buy',
                            date=buy_product.buy_date,
                            quantity=buy_product.buy_quantity,
                            price=int(quantity)*product.pro_price
                        )
                        product.crt_quantity += int(quantity)
                        product.save()
                return JsonResponse({'success': True, 'message': 'Stock added successfully.'}, status=200)
            except Exception as e:
                return JsonResponse({'success': False, 'message': f'Error: {str(e)}'})
    products = Product.objects.all() # filter the product details
    suppliers = Supplier.objects.all() # filter the supplier details
    return render(request,"add_stock.html",{"products":products,"suppliers":suppliers})

## sell products from the stock
def selling_product(request): 
    if request.method == "POST":
        try:
            buyer_name = request.POST.get("customerName", "")
            product_id = request.POST.get("product_id", "").strip()
            payment_method = request.POST.get("paymentMethod", "").strip()
            quantity = request.POST.get("quantity")
            payment_value = request.POST.get("paymentValue")
            sell_date = request.POST.get("date", "").strip()
            if payment_method == "cash" or payment_method == "online":
                auto_pay_id=id_generator()
                Payment.objects.create(
                    pay_id=auto_pay_id,
                    type=payment_method,
                    amount=int(payment_value),
                    pay_date=sell_date)
                payment=Payment.objects.get(pay_id=auto_pay_id)
                product=Product.objects.get(pro_id=product_id)
                auto_sell_id=id_generator()
                Sell_Product.objects.create(
                    sell_id=auto_sell_id,
                    sell_name=buyer_name,
                    pro_id=product,
                    sell_quantity=quantity,
                    sell_date=sell_date,
                    pay_id=payment)
                sell_product=Sell_Product.objects.get(sell_id=auto_sell_id)
                Stock.objects.create(
                    sell_id=sell_product,
                    sto_id=id_generator(),
                    pro_id=product,
                    type='Sold',
                    date=sell_product.sell_date,
                    quantity=sell_product.sell_quantity,
                    price=int(quantity)*product.pro_price
                )
                product.crt_quantity -= int(quantity)
                product.save()
            else:
                product=Product.objects.get(pro_id=product_id)
                auto_sell_id=id_generator()
                Sell_Product.objects.create(
                    sell_id=auto_sell_id,
                    sell_name=buyer_name,
                    pro_id=product,
                    sell_quantity=quantity,
                    sell_date=sell_date)
                sell_product=Sell_Product.objects.get(sell_id=auto_sell_id)
                Stock.objects.create(
                    sell_id=sell_product,
                    sto_id=id_generator(),
                    pro_id=product,
                    type='Sold',
                    date=sell_product.sell_date,
                    quantity=sell_product.sell_quantity,
                    price=int(quantity)*product.pro_price
                )
                product.crt_quantity -= int(quantity)
                product.save()
            return JsonResponse({'success': True, 'message': 'Stock added successfully.'}, status=200)
        except Exception as e:
                return JsonResponse({'success': False, 'message': f'Error: {str(e)}'})
    products = Product.objects.all() # filter the product details
    return render(request,"sell_products.html",{"products":products})

## view current details of the stock
def stock_details(request):
    products = Product.objects.all()
    return render(request,"stock_details.html",{"products":products})

def get_stock_history(request):
    product_id = request.GET.get('product_id')
    if not product_id:
        return JsonResponse({'error': 'Product ID is required'}, status=400)
    try:
        product = Product.objects.get(pro_id=product_id)
        stocks = Stock.objects.filter(pro_id=product).order_by("-date")
        stock_data = [
            {
            "date":stock.date.strftime("%Y-%m-%d"),
            "transaction_type":stock.type,
            "product_name":product.pro_name,
            "quantity":stock.quantity,
            "price":stock.price
        }
        for stock in stocks
        ]
        return JsonResponse({"history": stock_data}, status=200)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
def payments(request):
    suppliers = Supplier.objects.all() # filter the supplier details
    return render(request,"payments.html",{"suppliers":suppliers})

## view the payment details
def payment_details(request):
    if request.method == "POST":
        try:
            # Parse JSON data from request body
            data = json.loads(request.body)

            # Extract data from JSON
            payer_name = data.get('payerName')
            custom_buyer_name = data.get('customBuyerName')
            amount = data.get('amount')
            payment_method = data.get('payment_method')
            date = data.get('date')
            print(payer_name)
            # Validate and process data
            if not payer_name or not amount or not payment_method or not date:
                return JsonResponse({'error': 'All fields are required.'}, status=400)

            # Save to database (example model: Payment)
            # payment = Payment.objects.create(
            #     payer_name=payer_name,
            #     amount=amount,
            #     type=payment_method,
            #     pay_date=date,
            # )

            # Respond with success
            return JsonResponse({'success': True, 'message': 'Payment added successfully.'})

        except Exception as e:
            return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=500)

    return render(request,"payment_details.html")

def get_payment_history(request):
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")
    try:
        stock_payments = Payment.objects.filter(pay_date__range=(start_date, end_date)).order_by('pay_date')
        payment_data = [
                {
                    'date': payment.pay_date,
                    'supplier_name': payment.supp_id.supp_name if payment.supp_id else "N/A",
                    'amount': payment.amount,
                    'payment_method': payment.type
                }
                for payment in stock_payments
            ]

        return JsonResponse({"payment_data":payment_data}, status=200)
    
    except Exception as e:
        return JsonResponse({'error': 'An error occurred while fetching payment history.'}, status=500)
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
        product = Product.objects.get(pro_id=product_id)
        return JsonResponse({
            'product_id': product.pro_id,
            'product_name': product.pro_name,
            'quantity': product.crt_quantity,
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
