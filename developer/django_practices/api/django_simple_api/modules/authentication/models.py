from django.db import models


class UserPin(model.Models):
    email = models.EmailField(max_length=50)
    pin = models.CharField(max_length=6)
    
