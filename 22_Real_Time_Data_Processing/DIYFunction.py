from datetime import datetime
import boto3
import os
import base64
import json

dynamodb = boto3.client('dynamodb')
output_table = os.environ.get('OUTPUT_TABLE_NAME')


def handler(event, context):
    # Response will be a list of records.
    response = {
        "records": []
    }

    for record in event['Records']:

        payload = base64.b64decode(record.get('kinesis').get('data')).decode('utf-8')
        print(payload)
        payload_values = payload.split(",")

        try:
            dynamodb.put_item(TableName=output_table,
                              Item={
                                  'timestamp': {
                                      'S': str(datetime.now())
                                  },
                                  'location': {
                                      'S': payload_values[0].replace('"', '')
                                  },
                                  'max_wind_speed': {
                                      'S': payload_values[1]
                                  }
                              })
            response['records'].append({
                'recordId': record.get('recordId'),
                'result': 'Ok'
            })
        except:
            response['records'].append({
                'recordId': record.get('recordId'),
                'result': 'DeliveryFailed'
            })

    return response