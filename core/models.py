from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=255)
    is_expences = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        INCOME = "income", "Income"
        EXPENSE = "expense", "Expense"
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='transactions')
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='transaction_user')
    transaction_type = models.CharField(choices=TransactionType, max_length=50)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
