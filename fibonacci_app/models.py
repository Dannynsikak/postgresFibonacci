from django.db import models

# Create your models here.
class FIbonacci(models.Model):
    fibonacci_value = models.BigIntegerField()

    def __str__(self):
        return str(self.fibonacci_value)