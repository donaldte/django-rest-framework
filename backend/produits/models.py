from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    
    
    def get_price(self):
        return f'{self.price} FCFA'
    
    
    
    def get_discount(self):
        return self.price -10
   