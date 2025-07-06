from django.urls import path
from .views import hello_world, submit_expense,get_all_expenses,delete_expense  # import your views

urlpatterns = [
    path('test/', hello_world),              
    path('submit-expense/', submit_expense),
    path('get-expenses/', get_all_expenses),
    path('delete-expense/<int:expense_id>/', delete_expense),  
]
