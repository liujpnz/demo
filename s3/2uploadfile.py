import boto3


upload_filename = 'input.csv'
input_bucket_name ='jasons-python-input'
output_bucket_name ='jasons-python-output'

# Create an S3 client
s3 = boto3.client('s3')


# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
s3.upload_file(upload_filename, input_bucket_name, upload_filename)

json_object = s3.get_object(Bucket=input_bucket_name, Key=upload_filename)

#get jason reader
jsonFileReader = json_object['Body'].read()

print (type(json_object['Body']))





# Delete file
s3.delete_object(Bucket=input_bucket_name, Key=upload_filename)






#clean environment
#s3.delete_bucket(Bucket=input_bucket_name)
