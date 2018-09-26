import boto3


upload_filename = 'upload.csv'
input_bucket_name ='jasons-python-input'
output_bucket_name ='jasons-python-output'

# Create an S3 client
s3 = boto3.client('s3')

# Call S3 to list current buckets
response = s3.list_buckets()


for bucket in response['Buckets']:
    print (bucket['Name'])


# Get a list of all bucket names from the response
buckets = [bucket['Name'] for bucket in response['Buckets']]

# Print out the bucket list
print("Bucket List: %s" % buckets)



# Delete S3 file
s3.delete_object(Bucket=input_bucket_name, Key=upload_filename)



#clean environment
s3.delete_bucket(Bucket=input_bucket_name)
