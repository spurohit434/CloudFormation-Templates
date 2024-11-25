# import json

# print('Loading fucntion')

# def lambda_handler(event, context):
#     #print("Received event: " + json.dumps(event, indent=2))
#     print("value1 = " + event['key1'])
#     print("value2 = " + event['key2'])
#     print("value3 = " + event['key3'])
#     return event['key1']
#     #raise Exception('Something went wrong')


#  function for the lambda function with api gateway
import boto3
import json
import os

region_name = os.environ['REGION_NAME']
dynamo = boto3.client('dynamodb', region_name=region_name)
table_name = os.environ['TABLE_NAME']

print('Loading function')

def respond(err, res=None):
    return{
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers':{
            'Content-Type': 'application/json'
        },
    }

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    scan_result = dynamo.scan(Table_name=table_name)
    return respond(None, res=scan_result)