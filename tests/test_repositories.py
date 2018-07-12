from unittest import TestCase
from app.repositories import Repo

class TestRepo(TestCase):
    def test_repo_spec(self):
        repo = Repo()
        # The repository class will hold a list of tweets
        self.assertIsInstance(repo.tweets, list)
        # empty at first
        self.assertEqual(len(repo.tweets), 0)
        # will add new tweets
        tweet_msg = "This is a tweet message"
        repo.add_tweet(tweet_msg)
        self.assertEqual(len(repo.tweets), 1)
        # it will automatically assign to it an auto-incremented id (starting at 1).
        self.assertEqual(repo.tweets[0].id, 1)
        # it should allow to get a tweet based on its id.
        self.assertIsIn(tweet_msg, repo.tweets[0].text)
