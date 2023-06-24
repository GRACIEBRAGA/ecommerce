from django.db import models

# Create your models here.
from django.db import models


FORMA_DE_PAGAMENTO_CHOICES = (
    ("CRÉDITO", "Crédito"),
    ("DEBITO", "Débito"),
    ("PIX", "pix"),
    ("BOLETO", "Boleto"),
)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    customer_address = models.CharField(max_length=200)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.customer_name} - {self.date_ordered}"

class Pagamento(models.Model):
    forma_pagamento = models.CharField(null=False, choices=FORMA_DE_PAGAMENTO_CHOICES, max_length=20)