#insert and get record into Customers table using put_item/get_item api

from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Customers')

customerid = "C01"
name = "Jason"
address = "24 Milton Rd"


response = table.put_item(
   Item={
        'custid': customerid,
        'name': name,
        'address': address,
    }
)

print("PutItem succeeded:")

result = table.get_item(Key={'custid':'C01'})

#print(type(result['Item']))

#print(result['Item'])


print(result['Item']['custid'], ":", result['Item']['name'], ":", result['Item']['address'])

#print(json.dumps(response, indent=4, cls=DecimalEncoder))
