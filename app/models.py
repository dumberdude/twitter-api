from datetime import datetime

class Tweet(object):
    def __init__(self, msg):
        self.id = None
        self.text = msg
        self.created_at = str(datetime.now())
