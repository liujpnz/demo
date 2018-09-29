#delete s3 object 

import boto3



#default input values
filename = 'transactions.json'
bucket_name ='jasons-python-output'

# Create an S3 client
s3 = boto3.client('s3')

bucket_name = input("bucket name: [" + bucket_name + "]") or bucket_name
print (bucket_name)

while True:

    filename = input("delete file name: [" + filename + "]") or filename
    
    if filename == "exit":
        break

    print (filename)

    # Delete file
    s3.delete_object(Bucket=bucket_name, Key=filename)

    print("%s is deleted." % filename)
