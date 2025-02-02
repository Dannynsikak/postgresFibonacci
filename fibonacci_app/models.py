from django.db import models
from decimal import Decimal

# Create your models here.
class Fibonacci(models.Model):
    fibonacci_value = models.DecimalField(max_digits=100, decimal_places=0)

    def __str__(self):
        return str(self.fibonacci_value)