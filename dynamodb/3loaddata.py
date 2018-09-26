#batch load json file into dynamodb Transactions table


from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb')

transactions = dynamodb.Table('Transactions')
customers = dynamodb.Table('Customers')

with open("transactions.json") as json_file:
    records = json.load(json_file, parse_float = decimal.Decimal)
   
    #print(type(records))
    #print(records)

    for record in records.values():
        print (record)
        print(type(record))

        txnid = record['txnid']
        
        custid = record['custid']
        name = record['name']
        address = record['address']
        txndate = record['txndate']
        amount = int(record['amount'])

        print("Processing Transaction log:", txnid )
        

        try:
            #insert transaction log 
            transactions.put_item(
                Item={
                    'txnid': txnid,
                    'custid': custid,
                    'name': name,
                    'tnxdate': txndate,
                    'amount': amount,
                 }
            )

            #insert customer info
            customers.put_item(
                Item={
                    'custid': custid,
                    'name': name,
                    'address': address,
                 }
            )

        except Exception as e:
            print(e)
            print("ERROR: insert data into dynamodb".format(e))


print("finish process transaction log")
