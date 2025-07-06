from django.db import models

# Create your models here.

class Expense(models.Model):
    description = models.CharField(max_length=255)
    amount = models.FloatField()
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.description} - ₹{self.amount}"