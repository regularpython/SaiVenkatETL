import json

# import requests


def lambda_handler(event, context):
    print('Hi This is Venky')

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
