#delete bucket using boto3 api, make sure empty bucket first

import boto3

#specify bucket name
input_bucket_name ='jasons-python-input'
output_bucket_name ='jasons-python-output'

# Create an S3 client
s3 = boto3.client('s3')


#Delete speicified bucket
s3.delete_bucket(Bucket=input_bucket_name)
print("%s bucket deleted." % input_bucket_name)

s3.delete_bucket(Bucket=output_bucket_name)
print("%s bucket deleted." % output_bucket_name)
