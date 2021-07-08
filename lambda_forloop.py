import boto3

def lambda_handler(event, context):
    quakes = event['features']

    for quake in quakes:
        bucket = quake
        json_file_name = quake['id']
        print(json_file_name)
    return 'Hello from Lambda'