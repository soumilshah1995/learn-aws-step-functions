import json
import random


def lambda_handler(event, context):

    number = random.randint(1,10)
    if number < 5:
        raise Exception("Game Over")
    else:
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }
