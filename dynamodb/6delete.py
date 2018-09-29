#delete record with specified key/value

from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb')


#define default values
table = 'Customers'
key = 'custid'
value = 'C01'

table = input("table: [" + table + "]") or table
tab = dynamodb.Table(table)

#delete item with specified key
while True:

    key = input("key: [" + key + "]") or key
    
    if key  == "exit":
        break

    value = input("value: [" + value + "]") or value

    print (key + ":" + value)
    
    tab.delete_item(Key={key:value})


    print(key + ":" + value +" is deleted.")

