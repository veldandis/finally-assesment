from django.urls import path
from ..views import transaction_views as views


urlpatterns = [

    path('add/', views.addTransaction, name='addTransaction'),
    path('allTransactions/', views.getAllTransactions, name='allTransactions'),
    path('transactions/<int:accountId>/', views.getAllTransactionsByAccount, name='transactionsByAccountId'),
]