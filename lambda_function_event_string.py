def lambda_handler(event, context):
    print(str(event))
    return 'Hello from Lambda!'