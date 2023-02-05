print('## a1')
import json
print('## a2')
import generate_image
print('## a3')
import notion_api
print('## a4')

def handler(event, context):
    body = event["body-json"]
    client = body["client"]
    result = f"Hello, {client}"

    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }