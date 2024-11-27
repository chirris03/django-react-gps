from django import forms
from .models import Expense, Consumption, DiscardedItem

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['user', 'product', 'quantity']

class ConsumptionForm(forms.ModelForm):
    class Meta:
        model = Consumption
        fields = ['user', 'product', 'quantity']

class DiscardedItemForm(forms.ModelForm):
    class Meta:
        model = DiscardedItem
        fields = ['user', 'product', 'quantity', 'reason']
