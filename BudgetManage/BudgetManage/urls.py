"""BudgetManage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from budget.views import(
    base,
    MethodListView, MethodCreateView,
    CategoryCreateView, CategoryListView, CategoryDeleteView,CategoryUpdateView,
    SpendingCreateView, SpendingListView, SpendingUpdateView, SpendingDeleteView,
    IncomeCreateView, IncomeListView, IncomeUpdateView, IncomeDeleteView,
    SummaryView,
)
from users.views import(
    SignUpView,
)

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),
    #Base
    path('', base, name='index'),
    #savingmethod
    path('budget/methods/create/', MethodCreateView.as_view(), name='method_create'),
    path('budget/methods/list/', MethodListView.as_view(), name='method_list'),
    #categories
    path('budget/category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('budget/category/list/', CategoryListView.as_view(), name='category_list'),
    path('budget/category/delete/<pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('budget/category/update/<pk>/', CategoryUpdateView.as_view(), name='category_update'),
    #Budget

    #Spending
    path('budget/spending/create/',SpendingCreateView.as_view(), name='spending_create'),
    path('budget/spending/list/',SpendingListView.as_view(), name='spending_list'),
    path('budget/spending/update/<pk>/',SpendingUpdateView.as_view(), name='spending_update'),
    path('budget/spending/delete/<pk>/',SpendingDeleteView.as_view(), name='spending_delete'),

    #Income
    path('budget/income/create/', IncomeCreateView.as_view(), name='income_create'),
    path('budget/income/list/', IncomeListView.as_view(), name='income_list'),
    path('budget/income/delete/<pk>/', IncomeDeleteView.as_view(), name='income_delete'),
    path('budget/income/update/<pk>/', IncomeUpdateView.as_view(), name='income_update'),

    #Summary
    path('budget/spendings/summary', SummaryView.as_view(), name='summary'),

    #Users App
    path('users/sign-up/', SignUpView.as_view(), name='sign_up'),


    path('success/',TemplateView.as_view(template_name='success.html'), name='success'),
]
