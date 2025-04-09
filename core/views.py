from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, FormView, UpdateView
from core.forms import RegisterModelForm, LoginForm, TransactionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Transaction

# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'core/home-page.html'



class RegisterCreatView(CreateView):
    queryset = User.objects.all()
    form_class = RegisterModelForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('login')


class LoginFormView(FormView):
    form_class = LoginForm
    template_name = 'core/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        users = {
            'password': form.cleaned_data.get('password'),
            'username': form.cleaned_data.get('username')
        }
        query = User.objects.filter(username=users.get('username'))
        if query.exists():
            user = query.first()
            if check_password(users.get('password'), user.password):
                login(self.request, user)
            else:
                messages.error(self.request, 'Password exist!')
                return redirect('login')
        else:
            messages.error(self.request, f'{users.get('username')} name exist! ')
            return redirect('login')
        return super().form_valid(form)

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')




class ExpenseTransactionCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Transaction
    form_class = TransactionForm
    template_name = 'core/expense.html'
    success_url = reverse_lazy('home')

class IncomeTransactionCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Transaction
    form_class = TransactionForm
    template_name = 'core/income.html'
    success_url = reverse_lazy('home')
