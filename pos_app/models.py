from django.db import models

# Create your models here.

class item(models.Model):
    item_name = models.CharField(max_length=30)
    item_price = models.PositiveIntegerField()
    stock_quantity = models.PositiveIntegerField()

class order(models.Model):
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)
    order_method = models.CharField(max_length=30)
    
class item_order(models.Model):
    item_id = models.ForeignKey(item, on_delete=models.CASCADE)
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    line_total = models.DecimalField(max_digits=10, decimal_places=2)
    item_order_qty = models.PositiveIntegerField()
