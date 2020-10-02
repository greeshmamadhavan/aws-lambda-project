# aws-lambda-project

What is Lambda?
Amazon Web Services (AWS) Lambda lets you run JavaScript (Node.js), Java & Python scripts/apps in Amazon's (virtually) infinitely-scalable cloud environment without having provision VM instances or other "orchestration"; Everything is dynamically auto-scaled so if you have 1 user or 1 billion you pay for usage.

Create a Serverless Computing Solution with AWS Lambda.
This repository contains a collection of steps and other hands on content that will guide you through building various serverless applications using AWS Lambda, Amazon SNS, Amazon S3 and IAM.

Project: Create an AWS Lambda function to count the number of words in a text file.

• Deploy and configure an AWS Lambda-based serverless computing solution.
• Use AWS console to develop the Lambda function in Python and to create its required resources.
• Report the word count in an email using an Amazon Simple Notificatin Service (SNS) topic and Optionally, send the result in an SMS (text) message also.
• Format the response message as follows:
  "The word count in the file <textFileName> is nnn".
• Specify the email subject line as: Word Count Result
• Automatically trigger the function when the text file is uploaded to an Amazon S3 bucket.
• Create an Identity and Access Management (IAM) role to give permission to the Lambda function to access Amazon S3 and Amazon SNS. Specifically, the role should have the following permissions:
  
  ‣ AWSLambdaBasicExecutionRole
  ‣ AmazonSNSFullAccess
  ‣ AmazonS3FullAccess
