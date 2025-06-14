import gzip
import json
import base64

def lambda_handler(event, context):
    # Step 1: Decode base64 string
    compressed_payload = base64.b64decode(event['awslogs']['data'])

    # Step 2: Decompress gzip
    uncompressed_payload = gzip.decompress(compressed_payload)

    # Step 3: Parse JSON string
    log_data = json.loads(uncompressed_payload)

    # Print log group and stream info
    print("Log Group:", log_data['logGroup'])
    print("Log Stream:", log_data['logStream'])

    # Step 4: Loop through log events
    for log_event in log_data['logEvents']:
        message = log_event['message']
        timestamp = log_event['timestamp']

        print(f"[{timestamp}] {message}")

        # Optional: only flag ERROR logs
        if "ERROR" in message:
            print(f"❗ ERROR detected: {message}")

    return {
        'statusCode': 200,
        'body': json.dumps('Log processing complete.')
    }
