from django.shortcuts import render

from .forms import ExpenseForm
# Create your views here.
def index(request):
    form = ExpenseForm()

    context = {
        'form':form
    }
    return render(request, 'myapp/index.html', context)