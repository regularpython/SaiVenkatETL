import boto3
import pandas as pd
from io import StringIO
import json


def lambda_handler(event, context):
    print(event)
    file_name = json.loads(event['Records'][0]['body'])['file_name']

    s3 = boto3.client('s3')

    # Bucket and file details
    bucket_name = 'carrentalsdata'
    s3_key = file_name
    download_path = 'D:/Students/Class Explanation/Regularpython AWS Project/1.AWS ETL Project/local-file.csv'

    response = s3.get_object(Bucket=bucket_name, Key=s3_key)
    csv_content = response['Body'].read().decode('utf-8')

    df = pd.read_csv(StringIO(csv_content))
    df.to_csv(download_path)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello Regularpython",
            # "location": ip.text.replace("\n", "")
        }),
    }
