from django.shortcuts import render
from budgetplanning.models import BudgetMethod
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView


# Create your views here.
class BudgetMethodListView(ListView):
