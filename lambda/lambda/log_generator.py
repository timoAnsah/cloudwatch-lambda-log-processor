def lambda_handler(event, context):
    print("INFO: Lambda started")
    print("ERROR: Something went wrong")
    return {
        'statusCode': 200,
        'body': 'Test logs written to CloudWatch'
    }
