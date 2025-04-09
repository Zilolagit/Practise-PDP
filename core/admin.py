from django.contrib import admin
from core.models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass