#upload object to bucket and get object content
import boto3
import json


upload_filename = 'upload.json'
input_bucket_name ='jasons-python-input'
output_bucket_name ='jasons-python-output'

# Create an S3 client
s3 = boto3.client('s3')


# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
s3.upload_file(upload_filename, input_bucket_name, upload_filename)
print("Upload succeed")


json_object = s3.get_object(Bucket=input_bucket_name, Key=upload_filename)

#get jason reader
jsonFileReader = json_object['Body'].read()

#return a dict
jsonDict = json.loads(jsonFileReader)

print("%s contents:" % upload_filename)
print(json.dumps(jsonDict))

