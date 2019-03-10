from flask import Flask, request

from src.sentiment import SentimentAnalyzer

app = Flask(__name__)

sa = SentimentAnalyzer()

@app.route('/', methods=['POST'])
def hello_world():
    val = sa.predict(list(request.form)[0])
    return ":)\n" if val == 1 else ":(\n"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

