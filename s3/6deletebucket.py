#delete bucket using boto3 api, make sure empty bucket first

import boto3

#default input values
bucket_name ='jasons-python-output'

# Create an S3 client
s3 = boto3.client('s3')


print ("bucket must be empty before deleted")
while True:

    bucket_name = input("bucket name: [" + bucket_name + "]") or bucket_name

    if bucket_name == "exit":
        break

    print (bucket_name)


    #Delete speicified bucket
    s3.delete_bucket(Bucket=bucket_name)
    print("%s bucket deleted." % bucket_name)

