#upload object to bucket and get object content
import boto3
import json

#default input values
upload_filename = 'transactions.csv'
input_bucket_name ='jasons-python-input'


input_bucket_name = input("bucket name: [" + input_bucket_name + "]") or input_bucket_name
print (input_bucket_name)


upload_filename = input("upload file name: [" + upload_filename + "]") or upload_filename
print (upload_filename)


# Create an S3 client
s3 = boto3.client('s3')


# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
s3.upload_file(upload_filename, input_bucket_name, upload_filename)
print("Upload succeed!")

