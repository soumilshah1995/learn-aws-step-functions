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



class FireHose(object):
    def __init__(self, access_keys, secret_keys, region=""):
        self.access_keys = access_keys
        self.secret_keys = secret_keys
        self.region = region
        self.__client = boto3.client(
            "firehose",
            aws_access_key_id=self.access_keys,
            aws_secret_access_key=self.secret_keys,
            region_name=self.region,
        )

    def publish_item(self, delivery_stream_name, json_data):
        response = self.__client.put_record(
            DeliveryStreamName=delivery_stream_name,
            Record={"Data": json.dumps(json_data)},
        )
        return response



def lambda_handler(event, context):

    """
    sample input expected
    { "prod": "R31", "dest-code": 9511, "quantity": 1344 }
    """
    print(event)
    event["message"] = datetime.datetime.now().__str__()

    AWS_ACCESS_KEY = "XXX"
    AWS_SECRET_KEY = "XXXXX"
    AWS_REGION_NAME = "us-east-1"

    helper = FireHose(
        access_keys=AWS_ACCESS_KEY,
        secret_keys=AWS_SECRET_KEY,
        region=AWS_REGION_NAME,
    )

    response = helper.publish_item(
        delivery_stream_name="XXXXXXX",
        json_data=event
    )

    return response

