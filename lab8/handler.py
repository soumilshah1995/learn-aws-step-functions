# must be called as we're using zipped requirements
try:
    import unzip_requirements
except ImportError:
    pass

import json


def step_1(event, context):

    response = {
        "statusCode": 200,
        "body": "Message from step 1"
    }
    return response

def step_2(event, context):

    response = {
        "statusCode": 200,
        "body": "Message from step 2"
    }
    return response


def error_state(event, context):
    print("I am in error state")
    response = {
        "statusCode": 200,
        "body": "I am Error "
    }
    return response