from django.db import models

class WarehouseModel(models.Model):
    product_name = models.CharField(max_length=100)
    available_qty = models.IntegerField()

    def __str__(self):
        return f'{self.product_name}'

class Sales(models.Model):
    product = models.ForeignKey(WarehouseModel, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()
    sale_date = models.DateField()

    def __str__(self):
        return f'Sale of { self.product.product_name} on {self.sale_date}'
