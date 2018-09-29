# Demo
##install python pip aws cli boto3

https://medium.com/@jacobsteeves/aws-lambda-from-the-command-line-7efab7f3ebd9
# Create a user group 'lambda_group'
$ aws iam create-group --group-name lambda_group
# Create a user 'lambda_user'
$ aws iam create-user --user-name lambda_user
# Add our user to the group
$ aws iam add-user-to-group --user-name lambda_user --group-name lambda_group
# Create a password for this user
$ aws iam create-login-profile --user-name lambda_user --password My!User1Login8P@ssword
# Create an CLI access key for this user
$ aws iam create-access-key --user-name lambda_user
# Save the Secret and Access Key's some where safe




# aws cli configuration


jason@Server:~/python$ aws configure
AWS Access Key ID [****************IVPA]: 
AWS Secret Access Key [****************vvoz]: 
Default region name [ap-southeast-2]: 
Default output format [None]: 



# git pull **


# 



Some basic Git commands are:
```
git status
git add
git commit
```


## 1.csv
python script to format specified csv file to json file.


## 2.s3
basic operations with aws s3 service using boto3 api, which includes 
  create/delete buckets
  upload/download/delete files
  read file contents

## 3.dynamodb
basic operations wit aws dynamodb service using boto3 api, which includes
  create/delete tables
  select/insert/update/delete records
  
## 4.app
building a serverless application using s3, dynamodb, sns, sqs and lambda function to linked those services together.
before start, create iam role with including 
steps.
  ### 1-createbucket.py
    create two buckets jason-python-input/jason-python-output with specified regions
  
  ### 2-create_table.py
    create three dynamodb tables customers/transactions/totalamount with specified key. 
    For transactions table, we should enable stream with new and old images for lambda funcations.
  
  ### 3-create sns topic, sqs service.
    subscribe this sns topic with email and sqs endpoints 
  
  ### 4-lambda
    before this step, you need to create iam role: S3-Cloudwatch-DynamoDB for lambda functions to access resource with           cloudwatch,s3, dynamodb and sns
    
    * FormatCSV.py
      when any .csv file upload to jason-python-input bucket, this function will be triggered to convert csv to json format,
      and then put json file to jason-python-output bucket.
    
    * S3-Json-Dynamodb.py
      when any .json file upload into jason-python-output bucket, this function will be triggered to read those upload json
      file, and insert records to customers and transactions table.
    
    * TransactionAlert.py
      when any record into transactions table, this function will be triggered to create or update values in totalamount
      summary table. If totalamount great than 1000, an message will send to sns topic.
    
    * sns subscrption
      sns topic will push new message to its subscription endpoints
        an alert email will received
        an message queue will push to sqs queue for further process.
      
  ### e. use cloudformation template file for auto deployment
     
     Now, using cloudformer.template can deploy a, b, c steps for this application.
     
     In further, this template can include iam role, lambda and specified parameter for some resource name. then the whole
     applocation can be intergrated with CI/CD process.
 
 To be continued...
    
    
