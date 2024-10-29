from flask import Flask, request
from predict import predict
from io import BytesIO
import re
import base64
from PIL import Image

def runApp():
    app = Flask(__name__)

    @app.route("/health-check")
    def health_check():
        return "OK"

    @app.route('/api/predict', methods=['POST'])
    def start():
        image_data = re.sub('^data:image/.+;(base64)?,', '', request.json['data'])
        image = Image.open(BytesIO(base64.b64decode(image_data)))
        image = predict(image)
        buffered = BytesIO()
        image.save(buffered, format="png")
        data = base64.b64encode(buffered.getvalue())
        return {
            'data': data
        }

    app.run(host="0.0.0.0", port=5500)
    return app

if __name__ == '__main__':
    runApp()
