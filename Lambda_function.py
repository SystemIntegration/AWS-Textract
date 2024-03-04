import boto3  # Import the boto3 library for AWS interaction
import json  # Import the json library for JSON data handling
import os  # Import the os library for operating system-level functionalities

# Initialize S3 and Textract clients
s3_client = boto3.client('s3')
textract_client = boto3.client('textract')

# Define the main Lambda function
def lambda_handler(event, context):
    try:
        # Extract bucket and object key from the event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        object_key = event['Records'][0]['s3']['object']['key']
        
        # Define output JSON file name
        output_json_key = object_key.split('.')[0] + '.json'
        
        # Define temporary file path
        tmp_file_path = '/tmp/' + os.path.basename(object_key)
        
        # Download file from S3 to Lambda's temporary directory
        s3_client.download_file(bucket_name, object_key, tmp_file_path)
        
        # Use Textract to extract text from the downloaded file
        with open(tmp_file_path, 'rb') as file:
            response = textract_client.analyze_document(Document={'Bytes': file.read()}, FeatureTypes=['TABLES', 'FORMS'])

        # Create JSON object with metadata and blocks information
        output_json = {
            "DocumentMetadata": response['DocumentMetadata'],
            "Blocks": response['Blocks']
        }
        
        # Write JSON object to a file in Lambda's temporary directory
        with open('/tmp/' + output_json_key, 'w') as json_file:
            json.dump(output_json, json_file, indent=4)
        
        # Upload JSON file to S3
        s3_client.upload_file('/tmp/' + output_json_key, bucket_name, output_json_key)
        
        # Print completion message
        print("Extraction completed and JSON file stored in S3.")
        
    except Exception as e:
        # Print error message and raise exception
        error_message = f"Error processing object {object_key} in bucket {bucket_name}: {e}"
        print(error_message)
        raise e
