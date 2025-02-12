from django.db import models
from datetime import date, timedelta


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
    recurrance_choices = [
        ('Once', 'Once'),
        ('Weekly', 'Weekly'),
        ('Biweekly', 'Biweekly'),
        ('Monthly', 'Monthly'),]
    userid = models.DecimalField(max_digits=10, decimal_places=0, default=1)
    created_at = models.DateField(default=date.today)
    catagory = models.CharField(max_length=20, choices=catagory_choices, default="")
    recurrance = models.CharField(max_length=10, choices=recurrance_choices, default="Once")
    description = models.TextField(max_length=50, default="", blank=True, null=True)
    income = models.CharField(choices=income_choices, max_length=10, default="Income")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    next_occurance = models.DateField(blank=True, null=True)

    def calculate_next_occurance(self):
        """
        calculate next occurance of record
        """
        if self.occurance != "Once":
            return None
        elif self.recurrance == "Weekly":
            return self.created_at + timedelta(weeks=1)
        elif self.recurrance == "Biweekly":
            return self.created_at + timedelta(weeks=2)
        elif self.recurrance == "Monthly":
            if self.created_at.month == 12:
                return self.created_at.replace(year=self.created_at.year + 1, month=1)
            else:
                return self.created_at.replace(month=self.created_at.month + 1)

    def __str__(self):
        return (f"{self.created_at}  {self.description}")

# Create your models here.

class monthly_record(models.Model):
    date = models.DateField(default=date.today)
    income = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    expense = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return (f"{self.date.month}  {self.date.year}")
