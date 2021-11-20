from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DetailView
from budget.forms import MethodForm
from budget.models import Method
from logging import getLogger

LOGGER = getLogger() ## show errors
# Create your views here.

#Create Method List View
class MethodListView(ListView):
    template_name = "method/create.html"
    model = Method
    context_object_name = "method_list"

#Create Method Create View
class MethodCreateView(CreateView):
    template_name = "method/list.html"
    form_class = MethodForm
    success_url = reverse_lazy("success")