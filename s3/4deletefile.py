import boto3


upload_filename = 'upload.json'
input_bucket_name ='jasons-python-input'
output_bucket_name ='jasons-python-output'

# Create an S3 client
s3 = boto3.client('s3')


# Delete file
s3.delete_object(Bucket=input_bucket_name, Key=upload_filename)

print("%s is deleted." % upload_filename)
