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
import datetime as dt


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createAccount(request):

    try:
        user = request.user
        data = request.data

        # 1. create an account
        # need to write code so that we can mainain accoutNumber unique. Tihis should be done similar to the email field of from django.contrib.auth.models import User
        account = Account.objects.create(
            user=user,
            accountNumber=data['accountNumber']
        )
        serializer = AccountSerializer(account, many=False)
        return Response(serializer.data)
    except Exception as e:
        print(e)
        return Response({'detail': 'Not able to perform operation due to exception: '+str(e)+' For the account number: ' + str(data['accountNumber'])}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyAccounts(request):
    user = request.user
    accounts = user.account_set.all()
    print("The type of _set.all() return is: "+str(type(accounts)))
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAccountById(request, pk):
    print("Inside getAccountById method")

    user = request.user

    try:
        account = Account.objects.get(_id=pk)
        if user.is_staff or account.user == user:
            serializer = AccountSerializer(account, many=False)
            return Response(serializer.data)
        else:
            Response({'detail': 'Not authorized to view this account'},
                     status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'detail': 'Account does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addTransaction(request, pk):

    user = request.user
    data = request.data

    # 1. Fetch the account first

    try:
        account = Account.objects.get(_id=pk)
        if user.is_staff or account.user == user:
            # serializer = AccountSerializer(account, many=False)
            # return Response(serializer.data)

            amount = int(data['amount'])
            if (account.current_balance-amount < 0 and data['transaction_type'] == "DEBIT"):
                Response({'detail': 'Insufficient balance in account, unable to complete transaction'},
                         status=status.HTTP_400_BAD_REQUEST)

            else:
                # 1. Create the transaction

                transaction = Transaction.objects.create(
                    user=user,
                    account=account,
                    transaction_type=data['transaction_type'],
                    amount=data['amount']
                )

                # 2. Update the account and save the account

                if (data['transaction_type'] == "DEBIT"):
                    account.current_balance = account.current_balance - \
                        int(data['amount'])
                    transaction.updated_balance = account.current_balance
                    transaction.save()
                    account.save()
                else:
                    account.current_balance = account.current_balance + \
                        int(data['amount'])
                    transaction.updated_balance = account.current_balance
                    transaction.save()
                    account.save()

                serializer = TransactionSerializer(transaction, many=False)
                return Response(serializer.data)

        else:
            Response({'detail': 'Not authorized to view this account'},
                     status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response({'detail': 'Account does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllTransactions(request):
    print("Inside the getAllTransactions")
    try:
        user = request.user
        print("Received user: " + user.email)
        transactions = user.transaction_set.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)
    except Exception as e:
        print(e)
        return Response({'detail': 'Bad request at getAllTransactions'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllTransactionsByAccount(request, pk):
    print("********************Inside the getAllTransactionsByAccount(request,pk) method***********************")
    user = request.user
    data = request.data

    transactions = []

    # retreive the account
    try:
        account = Account.objects.get(_id=pk)
        if user.is_staff or account.user == user:

            transactions = account.transaction_set.all()
            serializer = TransactionSerializer(transactions, many=True)

            # print("The type of a transaction is: "+str(type(transactions[0])))
            # print("The type of date time is: "+ str(type(transactions['date'])))

            return Response(serializer.data)

        else:
            Response({'detail': 'This account does not belong to the user'},
                     status=status.HTTP_401_UNAUTHORIZED)

    except Exception as e:

        print("Exception : "+str(e))
        return Response({'detail': 'Account does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTransactionBalanceByDate(request, pk, date):
    # This method gets the closing balance by date
    print("********************Inside the getTransactionBalanceByDate(request,pk) method***********************")
    user = request.user
    data = request.data

    transactions = []

    # retreive the account
    try:
        account = Account.objects.get(_id=pk)
        if user.is_staff or account.user == user:

            transactions = account.transaction_set.all()

            # lets first get the latest transaction first
            tempid = -1
            maxIndex = 0
            iterationCount = -1

            for transaction in transactions:
                iterationCount = iterationCount + 1
                if (date == str(transaction.date.date())):
                    j = transaction._id
                    if (j > tempid):
                        tempid = j
                        maxIndex = iterationCount

            maxTransaction = transactions[maxIndex]

            print("The obtained date is: "+date)
            print("The date in the max transaction is: " +
                  str(maxTransaction.date.date()))

            serializer = TransactionSerializer(maxTransaction, many=False)
            return Response(serializer.data)

        else:
            Response({'detail': 'This account does not belong to the user'},
                     status=status.HTTP_401_UNAUTHORIZED)

    except Exception as e:

        print("The received exception is : "+str(e))
        return Response({'detail': 'Account does not exist'}, status=status.HTTP_400_BAD_REQUEST)
