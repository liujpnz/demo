import json
import boto3

#connect to s3 and dynamodb
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    json_file_name = event['Records'][0]['s3']['object']['key']

    json_object = s3_client.get_object(Bucket = bucket, Key = json_file_name)

    #get jason reader
    jsonFileReader = json_object['Body'].read()

    #return a dict
    jsonDict = json.loads(jsonFileReader)

    #specify Customers and Transactions table
    customers = dynamodb.Table('Customers')
    transactions = dynamodb.Table('Transactions')
    
    
    for record in jsonDict.values():
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

            

   # print(bucket)
   # print(json_file_name)
   # print(str(event))

    return "Hello from Lambda"

