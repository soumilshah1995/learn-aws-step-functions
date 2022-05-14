import json
import datetime

def lambda_handler(event, context):

    """
    sample input expected
    { "prod": "R31", "dest-code": 9511, "quantity": 1344 }
    """
    print(event)

    new_data = event["time"] = datetime.datetime.now().__str__()
    return event
