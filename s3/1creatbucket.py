import boto3


upload_filename = 'upload.csv'
input_bucket_name ='jasons-python-input1'
output_bucket_name ='jasons-python-outputi1'

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



#create bucket
s3.create_bucket(Bucket=input_bucket_name,CreateBucketConfiguration={'LocationConstraint':'ap-southeast-2'})
s3.create_bucket(Bucket=output_bucket_name,CreateBucketConfiguration={'LocationConstraint':'ap-southeast-2'})



# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
s3.upload_file(upload_filename, input_bucket_name, upload_filename)



