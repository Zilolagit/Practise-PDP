from django.contrib import admin
from core.models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_expences')
    list_filter = ('is_expences', 'name')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display =  ("amount", "category_id", "user_id", "transaction_type", "description", "created_at")
    list_filter =  ("amount", "category_id", "user_id", "transaction_type", "created_at")
