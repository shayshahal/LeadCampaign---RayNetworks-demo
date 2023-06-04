from flask import Flask, request
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/')
def hello():
    return '<p>Hello, World!</p>'


@app.route("/webhooks", methods=['GET'])
def verifyWebHook():
    if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.verify_token') == os.getenv('VERIFY_TOKEN'):
        return request.args.get('hub.challenge')
    else:
        return 'did not verify'


if __name__ == '__main__':
    app.run(debug=True, port=3000)
