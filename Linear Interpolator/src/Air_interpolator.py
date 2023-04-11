import os
import json
import interpolate

errorResponse = '{ error: { "0": "BadInput" }}'
dataUrl = os.getenv("DATA_URL", "../data/textbook_values.csv")
interpolate.load(dataUrl)

def lambda_handler(event, context):
    T = 0.0
    body = json.loads(event["body"])
    try:
        T = float(body["temperature"])
        interpolated = interpolate.interpolate(T)
        return {
            'statusCode': 200,
            'body': interpolated.to_json() if interpolated is not None else errorResponse
        }
    except Exception as ex:
        return {
            'statusCode': '500',
            'body': repr(ex)
        }

    

