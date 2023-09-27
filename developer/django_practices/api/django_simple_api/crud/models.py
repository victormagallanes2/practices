from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=100,default='0', decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=100, default='0', decimal_places=2, blank=True)
    description = models.TextField(max_length=250, blank=True)
    picture = models.ImageField(upload_to='apis/products/', blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
