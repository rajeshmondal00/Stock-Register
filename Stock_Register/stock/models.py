from django.db import models

# Create your models here
class Product(models.Model):
    pro_id = models.CharField(max_length=20,primary_key=True)
    product_name = models.CharField(max_length=120)
    quantity = models.IntegerField()
    category = models.CharField(max_length=20)
    weight = models.IntegerField()

    def __str__(self):
        return self.product_name
    
class Buy_Product(models.Model):
    supp_id = models.CharField(max_length=20,primary_key=True)
    pro_id = models.ForeignKey(Product,max_length=20,on_delete=models.CASCADE)
    buy_quantity = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.supp_id
    
class Supplier(models.Model):
    supp_id = models.ForeignKey(Buy_Product,max_length=20,on_delete=models.CASCADE)
    supplier_name = models.CharField(max_length=120)

    def __str__(self):
        return self.supplier_name
    
class Sell_Product(models.Model):
    sell_id = models.CharField(max_length=20,primary_key=True)
    pro_id = models.ForeignKey(Product,max_length=20,on_delete=models.CASCADE)
    sell_quantity = models.ImageField()
    date = models.DateField()

    def __str__(self):
        return self.sell_id
    
class Buyer(models.Model):
    sell_id = models.ForeignKey(Sell_Product,max_length=20,on_delete=models.CASCADE)
    seller_name = models.CharField(max_length=120)

    def __str__(self):
        return self.seller_name