## Project Overview

This project demonstrates how to extract text from files using AWS Textract and Boto3, an AWS SDK for Python. It involves setting up an S3 bucket, configuring a Lambda function

## Steps

1. **Create S3 Bucket and Lambda Function:**
    - Create an S3 bucket for file uploads.
    - Set up a Lambda function to trigger on S3 bucket events.

2. **Permissions Setup:**
    - Assign the Lambda execution role with:
        - S3 get and put Access policy.
        - Textract read and write Access policy.

3. **Configure Trigger:**
    - Set up an S3 event trigger to invoke the Lambda function on new file uploads.

## Functionality

Upon file upload to the S3 bucket, the Lambda function is triggered. It initiates text extraction using AWS Textract, formats the extracted text into a JSON file, and uploads it back to the same S3 bucket.

## Setup Instructions

1. **S3 Bucket Creation:**
    - Log in to the AWS Management Console.
    - Navigate to the S3 service.
    - Create a new bucket with a unique name.

2. **Lambda Function Setup:**
    - Go to the Lambda service in the AWS Management Console.
    - Create a new Lambda function.
    - Configure the function with an existing execution role or create a new one with S3 and Textract permissions.
    - Write or upload the Lambda function code.

3. **Permissions Configuration:**
    - Navigate to the IAM service in the AWS Management Console.
    - Locate the role associated with the Lambda function.
    - Attach policies for S3 Full Access and Textract Full Access to the role.

4. **Trigger Configuration:**
    - Go to the S3 service in the AWS Management Console.
    - Select the bucket created in step 1.
    - Configure a new event trigger to invoke the Lambda function on file uploads.

## Advantages of AWS Textract

1. **Accurate Text Extraction:**
   - Textract employs machine learning algorithms to accurately extract text from scanned documents, images, and PDFs.

2. **Structured Data Output:**
   - It provides structured data output, making it easy to work with extracted information for further processing.

3. **Supports Multiple Document Types:**
   - Textract supports a variety of document types, including forms, tables, and plain text documents.

4. **Automatic Data Organization:**
   - Textract automatically identifies and organizes key data points, reducing the need for manual data entry.

## Use Cases of AWS Textract

1. **Document Digitization:**
   - Textract is ideal for converting paper documents into digital formats, facilitating efficient document management.

2. **Data Extraction from Forms:**
   - It is suitable for extracting data from structured forms, such as invoices, receipts, and surveys, streamlining data entry processes.

3. **Automated Data Analysis:**
   - Textract enables automated extraction of information for further analysis, improving decision-making processes.

4. **Enhanced Search Functionality:**
   - By extracting text, Textract enhances search functionality within documents, making it easier to find relevant information.

## Usage

1. Upload files to the S3 bucket.
2. The Lambda function automatically triggers on file upload.
3. Textract extracts text and formats it into a JSON file.
4. The JSON file is uploaded back to the S3 bucket.

## Support

For any issues or queries related to the R&D Demo Project, please contact [info@systemintegration.in].


