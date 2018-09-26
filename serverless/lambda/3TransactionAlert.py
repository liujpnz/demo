import json
import boto3

# Connect to SNS
sns = boto3.client('sns')
alertTopic = 'TransactionAlert'

#print (sns.list_topics()['Topics'][0]['TopicArn'])

snsTopicArn = [t['TopicArn'] for t in sns.list_topics()['Topics'] if t['TopicArn'].endswith(':' + alertTopic)][0]


# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb')
totalamount = dynamodb.Table('TotalAmount')

# This handler is executed every time the Lambda function is triggered
def lambda_handler(event, context):

  # dump event message
  print("Event received by Lambda function: " + json.dumps(event, indent=2))

  # For each transaction added, calculate the new Transactions Total
  for record in event['Records']:
    custid = record['dynamodb']['NewImage']['custid']['S']
    amount = int(record['dynamodb']['NewImage']['amount']['N'])

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

  return 'finish process'