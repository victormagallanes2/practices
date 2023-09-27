from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from location.models import Country


class User(models.Model):
    PUBLICATION_STATUS = (('borrador', 'borrador'), ('publicada', 'publicada'))
    email = models.EmailField(unique=True)
    picture = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=False)
    about_me = models.TextField(max_length=400, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    web_site = models.URLField(max_length=250, blank=True)
    twitter = models.CharField(max_length=32, blank=True)
    want_offers = models.BooleanField(default=True)
    quantity = models.DecimalField(max_digits=100,default='0', decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=16, choices=PUBLICATION_STATUS, default='borrador')
    autor = models.ManyToManyField(User, related_name='users_autor')
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(blank=True, null=True)
    tickets_min = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.email