import json
from datetime import datetime

def lambda_handler(event, context):
    print("Received Event:", json.dumps(event))
    processed = []

    for record in event.get("Records", []):
        body = record.get("body", "")
        print(f"[{datetime.utcnow().isoformat()}] Processing log message: {body}")
        processed.append(body)

    return {
        "statusCode": 200,
        "processed": len(processed)
    }
