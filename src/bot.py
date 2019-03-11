from src.sentiment import SentimentAnalyzer
import random

class Bot():
    def __init__(self):
        self.sa = SentimentAnalyzer()
        self.positive = [':)',';)',':D','XD']
        self.negative = [':(',':/',':\'(',':[']

    def get_reaction(self, signal):
        if signal:
            return random.choice(self.positive) + "\n"
        else:
            return random.choice(self.negative) + "\n"

    def get_response(self, input):
        signal = self.sa.predict(input)
        return self.get_reaction(signal)