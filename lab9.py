import json
import datetime
import os
import json
import boto3
import uuid

"""
{
  "ship-date": "2016-03-14T01:59:00Z",
  "detail": {
    "delivery-partner": "UQS",
    "shipped": [
      { "prod": "R1", "dest-code": 9511, "quantity": 1344 },
      { "prod": "S2", "dest-code": 9511, "quantity": 40 },
      { "prod": "R3", "dest-code": 9833, "quantity": 12 },
      { "prod": "R4", "dest-code": 9860, "quantity": 887 },
      { "prod": "R5", "dest-code": 9511, "quantity": 1220 },
      { "prod": "R6", "dest-code": 9860, "quantity": 887 },
      { "prod": "R7", "dest-code": 9511, "quantity": 1220 }
    ]
  }
}
"""

def lambda_handler(event, context):
    
    for payload in event.get("Items"):
        payload["time"] = datetime.datetime.now().__str__()
    
    return event
