from django.db import models

# Create your models here.
class Expense(models.Model):
    up_front_cost = models.DecimalField(max_digits=10, decimal_places=2)
    daily_cost = models.DecimalField(max_digits=10, decimal_places=2)
    daily_income = models.DecimalField(max_digits=10, decimal_places=2)
    installation_date = models.DateField()