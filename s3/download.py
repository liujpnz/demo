import boto3


upload_filename = 'transactions.json'
input_bucket_name ='jasons-python-input'
output_bucket_name ='jasons-python-output'

s3 = boto3.resource('s3')

s3.Bucket(output_bucket_name).download_file(upload_filename, 'download.json')
