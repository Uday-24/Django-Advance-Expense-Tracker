from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Sum

from .forms import ExpenseForm
from .models import Expense
# Create your views here.
def index(request):

    if request.method == "POST":
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()
            return redirect('index')


    expenses = Expense.objects.all()
    total_expense = expenses.aggregate(Sum('amount'))
    form = ExpenseForm()
    context = {
        'form':form,
        'expenses':expenses,
        'total_expense':total_expense,
    }
    return render(request, 'myapp/index.html', context)

def fetch_expense(request):
    expense_id = request.GET.get('id')

    expense = get_object_or_404(Expense, id = expense_id)

    data = {
        'name' : expense.name,
        'amount' : expense.amount,
        'category' : expense.category,
    }

    return JsonResponse(data)

def update_expense(request):
    if request.method == "POST":
        id = request.POST.get('id')

        expense = get_object_or_404(Expense, id = id)
        
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'status': 'success',
                'message' : 'Expense updated successfully'
            })
        else:
            return JsonResponse({
                'status': 'failed',
                'message' : 'Expense is not updated'
            })
        
    else:
        return redirect('index')


def delete_expense(request):
    if request.method == "POST":
        id = request.POST.get('id')
        expense = get_object_or_404(Expense, id=id)
        expense.delete()
        data = {
            'status': 'success',
            'message': 'Expense deleted successfully'
        }
        return JsonResponse(data)
    else:
        return redirect('index')