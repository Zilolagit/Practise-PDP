from django.urls import path
from core.views  import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('register/', RegisterCreatView.as_view(), name='register'),
    path('income/', IncomeTransactionCreateView.as_view(), name='income'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('expense/', ExpenseTransactionCreateView.as_view(), name='expense'),
]
