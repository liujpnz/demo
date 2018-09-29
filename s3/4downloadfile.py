import boto3


#default input values
filename = 'transactions.json'
bucket_name ='jasons-python-output'


bucket_name = input("bucket name: [" + bucket_name + "]") or bucket_name
print (bucket_name)


filename = input("download file name: [" + filename + "]") or filename
print (filename)



s3 = boto3.resource('s3')

s3.Bucket(bucket_name).download_file(filename, filename)

print("file download!")
