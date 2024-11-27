from django.shortcuts import render, redirect
from .models import Expense, Consumption, DiscardedItem
from .forms import ExpenseForm, ConsumptionForm, DiscardedItemForm

def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_success')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

def add_consumption(request):
    if request.method == "POST":
        form = ConsumptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consumption_success')
    else:
        form = ConsumptionForm()
    return render(request, 'expenses/add_consumption.html', {'form': form})

def add_discarded_item(request):
    if request.method == "POST":
        form = DiscardedItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discard_success')
    else:
        form = DiscardedItemForm()
    return render(request, 'expenses/add_discarded_item.html', {'form': form})
