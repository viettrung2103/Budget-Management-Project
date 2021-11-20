from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DetailView

from budget.forms import MethodForm

from budget.models import SavingMethod

from logging import getLogger

LOGGER = getLogger() ## show errors
# Create your views here.

def base(request):
    return render(
        request, template_name="base.html"
    )

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