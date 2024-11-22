import boto3
import json
import os
 
def lambda_handler(event, context):
    # Initialize S3 client
    s3 = boto3.client('s3')
    # S3 bucket and object details
    bucket_name = 'task-bucket-wg-v1'
    object_key = 'file.json'
    try:
        # Process each record in the DynamoDB stream
        for record in event['Records']:
            # Check if the record is an INSERT or MODIFY event
            if record['eventName'] in ['INSERT']:
                # Extract the new image from the DynamoDB stream
                new_image = record['dynamodb']['NewImage']
                # Convert DynamoDB JSON to Python dictionary
                updated_record = {k: list(v.values())[0] for k, v in new_image.items()}
                print(f"Updated DynamoDB Record: {updated_record}")
                # Serialize the record to JSON
                json_data = json.dumps(updated_record)
                # Replace the S3 object with the new record
                s3.put_object(Bucket=bucket_name, Key=object_key, Body=json_data)
                print(f"Successfully updated S3 object '{object_key}' with new data.")
        return {
            "statusCode": 200,
            "body": "Successfully processed DynamoDB stream and updated S3 object."
        }
    except Exception as e:
        print(f"Error processing DynamoDB stream or updating S3: {e}")
        return {
            "statusCode": 500,
            "body": f"Error: {e}"
        }


