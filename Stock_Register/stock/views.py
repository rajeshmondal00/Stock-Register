from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")

def add_stocks(request):
    return render(request,"add_stock.html")

def selling_product(request):
    return render(request,"sell_products.html")

def stock_details(request):
    return render(request,"stock_details.html")