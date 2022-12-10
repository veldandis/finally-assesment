from django.urls import path
from ..views import account_views as views


urlpatterns = [

    path('create/', views.createAccount, name='account-add'),
    path('myAccounts/', views.getMyAccounts, name='myAccounts'),
    path('alltransactions/', views.getAllTransactions, name='allTransactions'),
    path('transactionsById/<str:pk>/', views.getAllTransactionsByAccount,
         name='transactionsByAccountId'),
    path('closingBalanceForDate/accounts/<str:pk>/date/<str:date>/',
         views.getTransactionBalanceByDate, name='closingBalanceforDate'),
    path('addTransaction/<str:pk>/', views.addTransaction, name='tranactionById'),
    path('getAccountById/<str:pk>/', views.getAccountById, name='accountById'),

]
