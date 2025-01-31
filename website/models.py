from django.db import models
from datetime import date

# Create your models here.
class Record(models.Model):
    catagory_choices = [
        ('Food', 'Food'),
        ('Clothing', 'Clothing'),
        ('Health', 'Health'),
        ('Education', 'Education'),
        ('Shopping', 'Shopping'),
        ('Salary', 'Salary'),
        ('Travel', 'Travel'),
        ('Utility', 'Utility'),
        ('Housing', 'Housing'),
        ('Transportation', 'Transportation'),
        ('Entertainment', 'Entertainment'),
        ('Gifts', 'Gifts'),
        ('Other', 'Other'),]
    income_choices = [
        ('Income', 'Income'),
        ('Expense', 'Expense'),]
    userid = models.DecimalField(max_digits=10, decimal_places=0, default=1)
    created_at = models.DateField(default=date.today)
    catagory = models.CharField(max_length=20, choices=catagory_choices, default="")
    description = models.TextField(max_length=50, default="", blank=True, null=True)
    income = models.CharField(choices=income_choices, max_length=10, default="Income")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    def __str__(self):
        return (f"{self.created_at}  {self.description}")

# Create your models here.
