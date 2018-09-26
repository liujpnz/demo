#delete record with specified key/value

from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb')

customers = dynamodb.Table('Customers')


customers.delete_item(Key={'custid':'C01'})
