from app.models import Tweet
class Repo(object):
    def __init__(self):
        self.tweets = []

    def add_tweet(self, text):
        self.tweets.append(Tweet(text))
