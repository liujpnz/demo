#using query method to get data from dynamodb

from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb')

customers = dynamodb.Table('Customers')

print("Customers Records:")

response = customers.query(
    KeyConditionExpression=Key('custid').eq('C01')
)

for i in response['Items']:
    print(i['custid'], ":", i['name'], ":", i['address'])
