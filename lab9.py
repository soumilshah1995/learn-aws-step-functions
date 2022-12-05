import json
import datetime
import os
import json
import boto3
import uuid

def lambda_handler(event, context):
    
    for payload in event.get("Items"):
        payload["time"] = datetime.datetime.now().__str__()
    
    return event
