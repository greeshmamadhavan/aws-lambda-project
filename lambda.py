import boto3
def lambda_handler(event, content):
	s3 = boto3.client('s3')
	sns = boto3.client('sns')
	data = s3.get_object(Bucket='awslambdatrigger1', Key='wordcount.txt')
	contents = data['Body'].read().decode('utf-8')
	count = len(contents.split())
	topic_arn= topicArn
	message = 'The word count in the file wordcount.txt is: ' + str(count)
	sns.publish(TopicArn=topic_arn, Message=message)
	return(message + ' <-- This message has been sent to subscribers.')