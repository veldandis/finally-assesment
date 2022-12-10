from django.shortcuts import render
from django.http import JsonResponse
#from .products import products
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from base.models import *
from base.serializers import *

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework import status

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addTransaction(request):
    user = request.user
    data = request.data
    accountId = int(data['accountId'])
    print("Received accountId "+ str(accountId)+" With type: "+ str(type(accountId)))

    #1. Fetch the account first

    try:
        retreivedAccount = Account.objects.get(_id=accountId)

        if user.is_staff or retreivedAccount.user == user:
            serializer = AccountSerializer(account, many=False)
            return Response(serializer.data)
        #account = Account.objects.get(_id=pk)        
        # if user.is_staff or retreivedAccount.user == user:
            
        #     amount = int(data['amount'])

        #     if(account.current_balance-amount<0 and data['transaction_type'] == "DEBIT"):
        #         Response({'detail': 'Insufficient balance in account, unable to complete transaction'},
        #                     status=status.HTTP_400_BAD_REQUEST)

        #     else:
        #         #1. Create the transaction
                
        #         transaction = Transaction.objects.create(
        #             user = user,
        #             account = retreivedAccount,
        #             transaction_type = data['transaction_type'],
        #             amount = data['amount']
        #         )

        #         #2. Update the account and save the account

        #         if(data['transaction_type'] == "DEBIT"):
        #             retreivedAccount.current_balance = retreivedAccount.current_balance - data['amount']

        #         else:
        #             retreivedAccount.current_balance = retreivedAccount.current_balance + data['amount']

        # else:
        #     Response({'detail': 'This account does not belong to the user'},
        #              status=status.HTTP_401_UNAUTHORIZED)
    except:
        return Response({'detail': 'Account does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllTransactions(request):
    user = request.user
    transactions = user.transaction_set.all()
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllTransactionsByAccount(request,accountId):
    user = request.user
    data = request.data

    transactions = []

    # retreive the account
    try:
        retreivedAccount = Account.objects.get(_id=accountId)
        if user.is_staff or retreivedAccount.user == user:
            
            transactions = retreivedAccount.transaction_set.all()

        else:
            Response({'detail': 'This account does not belong to the user'},
                     status=status.HTTP_401_UNAUTHORIZED)
    except:
        return Response({'detail': 'Account does not exist'}, status=status.HTTP_404_NOT_FOUND)

    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)

