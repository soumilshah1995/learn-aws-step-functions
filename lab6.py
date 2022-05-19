import json
import datetime
import os
import json
import boto3
import uuid


def lambda_handler(event, context):

    """
    sample input expected
    { "prod": "R31", "dest-code": 9511, "quantity": 1344 }
    """
    print(event)
    event["time"] = datetime.datetime.now().__str__()
    return event
