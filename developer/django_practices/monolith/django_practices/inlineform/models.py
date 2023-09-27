from django.db import models
from ..crud.models import Course

class Invoice(models.Model):
    number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name


class InvoiceProduct(models.Model):
    relationship = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    name = models.ForeignKey('crud.Course', on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.DecimalField(max_digits=100, default='0',
                                   decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=100, default='0', decimal_places=2,
                                blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name