from flask import Flask, request

from src.bot import Bot
from src.sentiment import SentimentAnalyzer

app = Flask(__name__)
bot = Bot()

@app.route('/', methods=['POST'])
def hello_world():
    input = list(request.form)[0]
    return bot.get_response(input)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

