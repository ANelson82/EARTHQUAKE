import boto3
import json
from decimal import Decimal

s3_client = boto3.client('s3')
dynambodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    json_file_name = event['Records'][0]['s3']['object']['key']
    json_object = s3_client.get_object(Bucket=bucket, Key=json_file_name)
    jsonFileReader = json_object['Body'].read()
    jsonDict = json.loads(jsonFileReader, parse_float=Decimal)
    table = dynambodb.Table('earthquakeDB02')
    table.put_item(Item=jsonDict)
    return 'Hello from Lambda!'