from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from django.db.models import Sum

from budget.forms import MethodForm, CategoryForm, SpendingForm, IncomeForm, RecordForm

from budget.models import SavingMethod, Category, Spending, Income, Record

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
    success_url = reverse_lazy("summary")

##CRUD for Category:
class CategoryCreateView(CreateView):
    template_name = "categories/create.html"
    form_class = CategoryForm
    success_url = reverse_lazy('summary')

class CategoryListView(ListView):
    template_name = "categories/list.html"
    model = Category
    context_object_name = "category_list"

class CategoryDeleteView(DeleteView):
    template_name = 'categories/confirm_delete.html'
    model = Category
    success_url = reverse_lazy('summary')

class CategoryUpdateView(UpdateView):
    template_name = "categories/create.html"
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("summary")

#CRUD for Spending:
class SpendingCreateView(CreateView):
    template_name = "spendings/create.html"
    form_class = SpendingForm
    success_url = reverse_lazy('summary')

class SpendingListView(ListView):
    template_name = "spendings/list.html"
    model = Spending

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['expenses'] = Spending.objects.all() # get a query of all expenses
        total_expenses = context['expenses'].aggregate(Sum('amount'))  #sum
        context['total_expenses'] = total_expenses

        return context

class SpendingUpdateView(UpdateView):
    template_name = "spendings/create.html"
    model = Spending
    form_class = SpendingForm
    success_url = reverse_lazy("summary")

class SpendingDeleteView(DeleteView):
    template_name = 'spendings/confirm_delete.html'
    model = Spending
    success_url = reverse_lazy('summary')

#CRUD for Income
class IncomeCreateView(CreateView):
    template_name = "incomes/create.html"
    form_class = IncomeForm
    success_url = reverse_lazy('summary')

class IncomeListView(ListView):
    template_name = "incomes/list.html"
    model = Income

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['incomes'] = Income.objects.all() # get a query of all expenses
        total_incomes = context['incomes'].aggregate(Sum('amount')) #summ
        context['total_income'] = total_incomes
        return context

class IncomeUpdateView(UpdateView):
    template_name = "incomes/create.html"
    model = Income
    form_class = IncomeForm
    success_url = reverse_lazy("summary")

class IncomeDeleteView(DeleteView):
    template_name = 'incomes/confirm_delete.html'
    model = Income
    success_url = reverse_lazy('summary')

#CRUD for Record
class RecordCreateView(CreateView):
    template_name = "records/create.html"
    form_class = RecordForm
    success_url = reverse_lazy('record_list')

class RecordListview(ListView):
    template_name = "records/list.html"
    model = Record
    context_object_name = "records"

    def get_queryset(self):
        return Record.objects.filter(user=self.request.user.profile)


class RecordDetailView(DetailView):
    template_name = "records/detail.html"
    model = Record
    context_object_name = 'record'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk'] # this is to get querry parameter
        # print(f' This is {pk}')
        # x = self.request.GET.get('x')# this is to get a query set
        # print(f' This is {x}')
        context = super().get_context_data(**kwargs)
        context['incomes'] = Income.objects.filter(record__id = pk)
        context['expenses'] = Spending.objects.filter(record__id = pk)
        records = Record.objects.filter(user=self.request.user.profile) # to get all the records from logged-in user
        profile = self.request.user.profile
        records = profile.records

        return context



class RecordUpdateView(UpdateView):
    template_name = "records/create.html"
    model = Record
    form_class = RecordForm
    success_url = reverse_lazy("record_list")

class RecordDeleteView(DeleteView):
    template_name = 'records/confirm_delete.html'
    model = Record
    success_url = reverse_lazy('record_list')


#This View will show the summary of the Budget
class SummaryView(ListView):
    template_name = "spendings/summary.html"
    context_object_name = "expenses"

    def get_queryset(self):
        return Spending.objects.all()

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['incomes'] = Income.objects.all()
        context['expenses'] = Spending.objects.all()

        total_incomes = context['incomes'].aggregate(Sum('amount')) #sumofincomes
        total_expenses = context['expenses'].aggregate(Sum('amount')) #sumofincomes
        saving = total_incomes['amount__sum'] - total_expenses['amount__sum'] #total incomes - total expense

        context['total_incomes'] = total_incomes
        context['total_expenses'] = total_expenses
        context['saving'] = saving  #
        return context

