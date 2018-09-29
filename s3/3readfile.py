#get object content from s3 bucket
import boto3
import json

#default input values
filename = 'transactions.json'
output_bucket_name ='jasons-python-output'


output_bucket_name = input("bucket name: [" + output_bucket_name + "]") or output_bucket_name
print (output_bucket_name)


filename = input("file name: [" + filename + "]") or filename
print (filename)


# Create an S3 client
s3 = boto3.client('s3')




json_object = s3.get_object(Bucket=output_bucket_name, Key=filename)

#get jason reader
jsonFileReader = json_object['Body'].read()

#return a dict
jsonDict = json.loads(jsonFileReader)

print("%s contents:" % filename)
print(json.dumps(jsonDict))

