from predict import predict
from io import BytesIO
import base64
from PIL import Image
import json
import re

def common_predict(data):
    data = re.sub('^data:image/.+;base64,', '', data)
    image = Image.open(BytesIO(base64.b64decode(data)))
    image = predict(image)
    buffered = BytesIO()
    image.save(buffered, format="png")
    data = base64.b64encode(buffered.getvalue())
    return data

def handler(event, context):
    return {
        'data': common_predict(event['data'])
    }

def function_url_invoke(event, context):
    body = json.loads(event["body"])
    data = common_predict(body['data'])
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "data": data.decode("utf-8")
        })
    }
