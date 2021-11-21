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
    MethodListView, MethodCreateView,
    CategoryCreateView, CategoryListView, CategoryDeleteView,CategoryUpdateView,
    SpendingCreateView, SpendingListView, SpendingUpdateView,
)

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),
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
    path('budget/spending/update/<pk>',SpendingUpdateView.as_view(), name='spending_update'),


    path('success/',TemplateView.as_view(template_name='success.html'), name='success'),
]
