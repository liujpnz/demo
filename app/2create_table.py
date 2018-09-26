#create dynamodb table, please specify tablename and key info

from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb')


customer_table = dynamodb.create_table(
    TableName='Customers',
    KeySchema=[
        {
            'AttributeName': 'custid',
            'KeyType': 'HASH'  #Partition key
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'custid',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", customer_table.table_status)



transaction_table = dynamodb.create_table(
    TableName='Transactions',
    KeySchema=[
        {
            'AttributeName': 'txnid',
            'KeyType': 'HASH'  #Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'txnid',
            'AttributeType': 'S'
        },
    ],
    StreamSpecification={
        'StreamEnabled': True,
        'StreamViewType': 'NEW_AND_OLD_IMAGES'
    },
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", transaction_table.table_status)



transaction_table = dynamodb.create_table(
    TableName='TotalAmount',
    KeySchema=[
        {
            'AttributeName': 'custid',
            'KeyType': 'HASH'  #Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'custid',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", transaction_table.table_status)
