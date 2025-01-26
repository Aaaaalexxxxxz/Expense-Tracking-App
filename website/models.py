from django.db import models
from datetime import date


# Create your models here.
class Record(models.Model):
    created_at = models.DateField(default=date.today)
    catagory = models.CharField(max_length=20, default="")
    description = models.TextField(max_length=50, default="", blank=True, null=True)
    income = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    def __str__(self):
        return (f"{self.created_at}  {self.description}")

# Create your models here.
