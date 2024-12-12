from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, blank = False, null = False, unique = True)
    type = models.CharField(max_length=100, blank = False, null = False)
    quality = models.IntegerField(default = 0)
    quantity = models.IntegerField(default = 0)
    timestamp = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.name

class LoyalCustomer(models.Model):
    name = models.CharField(max_length=100, blank = False, null = False, unique = True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)

    def __str__(self):
        return self.name