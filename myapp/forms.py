from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['up_front_cost', 'daily_cost', 'daily_income', 'installation_date']
