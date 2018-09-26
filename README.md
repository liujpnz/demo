# Demo
1.csv
python script to format specified csv file to json file.


2.s3
basic operations with aws s3 service using boto3 api, which includes 
  create/delete buckets
  upload/download/delete files
  read file contents

3.dynamodb
basic operations wit aws dynamodb service using boto3 api, which includes
  create/delete tables
  select/insert/update/delete records
  
4.app
building a serverless application using s3, dynamodb, sns, sqs and lambda function to linked those services together.
before start, create iam role with including 
steps.
  a. 1createbucket.py
    create two buckets jason-python-input/jason-python-output with specified regions
  
  b. 2create_table.py
    create three dynamodb tables customers/transactions/totalamount with specified key. 
    For transactions table, we should enable stream with new and old images for lambda funcations.
  
  c. create sns topic, sqs service.
    subscribe this sns topic with email and sqs endpoints 
  
  d. 3lambda
    before this step, you need to create iam role: S3-Cloudwatch-DynamoDB for lambda functions to access resource with           cloudwatch,s3, dynamodb and sns
    
    1FormatCSV.py
      when any .csv file upload to jason-python-input bucket, this function will be triggered to convert csv to json format,       and then put json file to jason-python-output bucket.
    
    2S3-Json-Dynamodb.py
      when any .json file upload into jason-python-output bucket, this function will be triggered to read those upload json         file, and insert records to customers and transactions table.
    
    3TransactionAlert.py
      when any record into transactions table, this function will be triggered to create or update values in totalamount           summary table. If totalamount great than 1000, an message will send to sns topic.
    
    4 sns subscrption
      sns topic will push new message to its subscription endpoints
      an alert email will received
      an message queue will push to sqs queue for further process.
      
  e. use cloudformation template file for auto deployment
     
     Now, using cloudformer.template can deploy a, b, c steps for this application.
     
     In further, this template can include iam role, lambda and specified parameter for some resource name. then the whole        applocation can be intergrated with CI/CD process.
 
 To be continued...
    
    
