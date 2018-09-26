#drop table using delete() api

from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb')

customers = dynamodb.Table('Customers')
transactions = dynamodb.Table('Transactions')
totalamount = dynamodb.Table('TotalAmount')


customers.delete()
transactions.delete()
totalamount.delete()
