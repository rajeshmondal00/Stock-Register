from django.db import models

# Create your models here
class Product(models.Model):
    pro_id = models.CharField(max_length=20, primary_key=True)
    pro_name = models.CharField(max_length=120)
    pro_price = models.IntegerField()
    crt_quantity = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return self.pro_name

class Supplier(models.Model):
    supp_id = models.CharField(max_length=20, primary_key=True)
    supp_name = models.CharField(max_length=120)

    def __str__(self):
        return self.supp_name

class Payment(models.Model):
    pay_id = models.CharField(max_length=20, primary_key=True)
    supp_id = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    TYPE_CHOICES = [
        ("cash", "Cash"),
        ("online", "Online")
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount = models.IntegerField()
    pay_date = models.DateField()

    def __str__(self):
        return f"Payer Name: {self.supp_id.supp_name}           Amount: {self.amount}           Date: {self.pay_date} "
    
class Buy_Product(models.Model):
    buy_id = models.CharField(max_length=20, primary_key=True)
    supp_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    pro_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    buy_quantity = models.IntegerField()
    buy_date = models.DateField()
    pay_id = models.ForeignKey(Payment, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.buy_id} - {self.pro_id.pro_name}"

class Sell_Product(models.Model):
    sell_id = models.CharField(max_length=20, primary_key=True)
    sell_name = models.CharField(max_length=120)
    pro_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    sell_quantity = models.IntegerField()
    sell_date = models.DateField()
    pay_id = models.ForeignKey(Payment, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.sell_name

class Stock(models.Model):
    sto_id = models.CharField(max_length=20, primary_key=True)
    pro_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    type_choice = [
        ("1", "Buy"),
        ("2", "Sold")
    ]
    type = models.CharField(max_length=5, choices=type_choice)
    date = models.DateField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    buy_id = models.ForeignKey(Buy_Product, on_delete=models.CASCADE, null=True, blank=True)
    sell_id = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Stock ID: {self.sto_id}"
