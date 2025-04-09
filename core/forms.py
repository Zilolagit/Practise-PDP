from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.forms import CharField, Form, Textarea, DateInput, TextInput, NumberInput, Select
from django.forms.models import ModelForm
from core.models import Transaction




class RegisterModelForm(ModelForm):
    class Meta:
        model=User
        fields='first_name','password','username'
    def clean_password(self):
        password=self.cleaned_data.get('password')
        hash=make_password(password)
        return hash

class LoginForm(Form):
    username=CharField(max_length=100)
    password=CharField(max_length=100)


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_type', 'amount', 'category_id', 'description', 'user_id']