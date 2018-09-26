import json
import csv
import StringIO
import boto3

#connect to s3
s3_client = boto3.client('s3')

output_bucket = 'jasons-python-output'
def lambda_handler(event, context):
    for r in event['Records']:
        s3 = r['s3']
        bucket = s3['bucket']['name']
        key = s3['object']['key']
        
        json_object = s3_client.get_object(Bucket = bucket, Key = key)

        #get jason reader
        body = json_object['Body'].read()

        file_obj = StringIO.StringIO(body)
        
        data = {}
        csvReader = csv.DictReader(file_obj)
        for csvRow in csvReader:
            id = csvRow["txnid"]
            data[id] = csvRow

        records = json.dumps(data, indent = 4)
        
        boto3.resource('s3').Object(output_bucket, key.replace('.csv', '.json')).put(Body=records)

    return 'OK'