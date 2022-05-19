"""
{
   "ship-date":"2016-03-14T01:59:00Z",
   "detail":{
      "delivery-partner":"UQS",
      "shipped":[
         {
            "prod":"R31",
            "dest-code":9511,
            "quantity":1344
         },
         {
            "prod":"S39",
            "dest-code":9511,
            "quantity":40
         },
         {
            "prod":"R31",
            "dest-code":9833,
            "quantity":12
         },
         {
            "prod":"R40",
            "dest-code":9860,
            "quantity":887
         },
         {
            "prod":"R40",
            "dest-code":9511,
            "quantity":1220
         }
      ]
   }
}

"""

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
