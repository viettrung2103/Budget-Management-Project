from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from django.db.models import Sum

from budget.forms import MethodForm, CategoryForm, SpendingForm

from budget.models import SavingMethod, Category, Spending

from logging import getLogger

LOGGER = getLogger() ## show errors
# Create your views here.

def base(request):
    return render(
        request, template_name="base.html"
    )
## CRUD for Saving Method
#Create Method List View
class MethodListView(ListView):
    template_name = "list.html"
    model = SavingMethod
    context_object_name = "method_list"

#Create Method Create View
class MethodCreateView(CreateView):
    template_name = "create.html"
    form_class = MethodForm
    success_url = reverse_lazy("success")

##CRUD for Category:
class CategoryCreateView(CreateView):
    template_name = "categories/create.html"
    form_class = CategoryForm
    success_url = reverse_lazy('success')

class CategoryListView(ListView):
    template_name = "categories/list.html"
    model = Category
    context_object_name = "category_list"

class CategoryDeleteView(DeleteView):
    template_name = 'categories/confirm_delete.html'
    model = Category
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    template_name = "categories/create.html"
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("category_list")

#CRUD for Spending:
class SpendingCreateView(CreateView):
    template_name = "spendings/create.html"
    form_class = SpendingForm
    success_url = reverse_lazy('success')

class SpendingListView(ListView):
    template_name = "spendings/list.html"
    model = Spending
    context_object_name = 'spending_list'

class SpendingUpdateView(UpdateView):
    template_name = "spendings/create.html"
    model = Spending
    form_class = SpendingForm
    success_url = reverse_lazy("spending_list")

class SpendingDeleteView(DeleteView):
    template_name = 'spendings/confirm_delete.html'
    model = Spending
    success_url = reverse_lazy('spending_list')

def totalspending(request):
    incomes = Spending.objects.filter(spendingtype=1)
    expenses = Spending.objects.filter(spendingtype=2)

    total_incomes= incomes.aggregate(Sum('amount'))
    total_expenses= expenses.aggregate(Sum('amount',Value=0))


    context = {
        'incomes':incomes,
        'expenses':expenses,
        'total_incomes':total_incomes,
        'total_expenses':total_expenses,

               }

    return render(
        request,'spendings/summary.html',context)