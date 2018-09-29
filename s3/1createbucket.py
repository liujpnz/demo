#using boto3 client api list and create new bucket with speicified region
import boto3


#default input values
input_bucket_name ='jasons-python-input'
output_bucket_name ='jasons-python-output'


input_bucket_name = input("input bucket name: [" + input_bucket_name + "]") or input_bucket_name
print (input_bucket_name)


input_bucket_name = input("output bucket name: [" + output_bucket_name + "]") or output_bucket_name
print (output_bucket_name)

# Create an S3 client
s3 = boto3.client('s3')

response = s3.list_buckets()



# Get a list of all bucket names from the response
buckets = [bucket['Name'] for bucket in response['Buckets']]

# Print out the bucket list
print("Bucket List: %s" % buckets)



#create bucket
s3.create_bucket(Bucket=input_bucket_name,CreateBucketConfiguration={'LocationConstraint':'ap-southeast-2'})
print("%s bucket created." % input_bucket_name)


s3.create_bucket(Bucket=output_bucket_name,CreateBucketConfiguration={'LocationConstraint':'ap-southeast-2'})
print("%s bucket created." % output_bucket_name)
