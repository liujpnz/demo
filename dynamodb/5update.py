#using json file to update record with update_item method
#when total transaction amount greater than 1000, send message aws SNS service

import boto3
import json
import decimal


dynamodb = boto3.resource('dynamodb')


# Connect to SNS
sns = boto3.client('sns')
alertTopic = 'TransactionAlert'

#print (sns.list_topics()['Topics'][0]['TopicArn'])

#get sns topic ARN
snsTopicArn = [t['TopicArn'] for t in sns.list_topics()['Topics'] if t['TopicArn'].endswith(':' + alertTopic)][0]



totalamount = dynamodb.Table('TotalAmount')

with open("transactions.json") as json_file:
    records = json.load(json_file, parse_float = decimal.Decimal)

    print(type(records))
    print(records)

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
            # Update the customer's total in the TransactionTotal DynamoDB table
            response = totalamount.update_item(
                Key={
                        'custid': custid
                    },
                #Adds the specified value to the item, if the attribute does not already exist(0)
                UpdateExpression="add totalamount :val",
                ExpressionAttributeValues={
                ':val': amount
                },

                #Returns only the updated attributes, as they appear after the UpdateItem operation.
                ReturnValues="UPDATED_NEW"
            )



            # Get the latest total amount
            latestAmount = response['Attributes']['totalamount']
            print(custid + " Latest account balance: " + format(latestAmount))
            

            #Check with alert value
            if latestAmount >1000:

                #SNS message
                message = '{"CustomerID": "'+ custid + '", ' + '"total amount": "' + str(latestAmount) + '"}'
                print(message)

                # Send message to SNS
                sns.publish(
                    TopicArn=snsTopicArn,
                    Message=message,
                    Subject='ALERT for total transaction amount',
                    MessageStructure='raw'
                )


        except Exception as e:
            print(e)
            print("ERROR: update totalamount table in dynamodb".format(e))


print("finish process transaction log")

