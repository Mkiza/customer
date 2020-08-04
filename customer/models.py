from django.db import models

# Create your models here.
class Customer(models.Model):
    #Character fields to store string
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    # __str__ method tells Djnago what to print when it needs to print out an instance of customer object
    def __str__(self):
        return self.name
