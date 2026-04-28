"""Twitter/X API v2 client wrapper."""
import os
import tweepy
from typing import Optional, Dict, Any

class TwitterClient:
    """Client for Twitter API v2."""
    
    def __init__(self, bearer_token: Optional[str] = None):
        """
        Initialize Twitter client.
        
        Args:
            bearer_token: Twitter API bearer token. If not provided, will try
                         to read from environment variable TWITTER_BEARER_TOKEN.
        """
        self.bearer_token = bearer_token or os.getenv("TWITTER_BEARER_TOKEN")
        if not self.bearer_token:
            raise ValueError(
                "Bearer token must be provided or set in TWITTER_BEARER_TOKEN environment variable"
            )
        self.client = tweepy.Client(bearer_token=self.bearer_token)
    
    def tweet(self, text: str) -> Dict[str, Any]:
        """
        Post a tweet.
        
        Args:
            text: Tweet text (max 280 characters).
            
        Returns:
            Dictionary containing tweet ID and text.
            
        Raises:
            tweepy.TweepyException: If tweet fails.
        """
        if len(text) > 280:
            raise ValueError("Tweet text exceeds 280 characters")
        
        response = self.client.create_tweet(text=text)
        return {
            "id": response.data["id"],
            "text": response.data["text"],
        }
    
    def get_tweet(self, tweet_id: str) -> Dict[str, Any]:
        """
        Retrieve a tweet by ID.
        
        Args:
            tweet_id: Tweet ID.
            
        Returns:
            Dictionary containing tweet details.
        """
        response = self.client.get_tweet(
            tweet_id,
            expansions=["author_id"],
            tweet_fields=["created_at", "public_metrics"],
        )
        tweet = response.data
        return {
            "id": tweet.id,
            "text": tweet.text,
            "author_id": tweet.author_id,
            "created_at": tweet.created_at,
            "public_metrics": tweet.public_metrics,
        }
    
    def get_user_tweets(self, user_id: str, max_results: int = 10) -> list:
        """
        Get recent tweets from a user.
        
        Args:
            user_id: Twitter user ID.
            max_results: Maximum number of tweets to return (default 10, max 100).
            
        Returns:
            List of tweet dictionaries.
        """
        response = self.client.get_users_tweets(
            user_id,
            max_results=max_results,
            tweet_fields=["created_at", "public_metrics"],
        )
        tweets = []
        if response.data:
            for tweet in response.data:
                tweets.append({
                    "id": tweet.id,
                    "text": tweet.text,
                    "created_at": tweet.created_at,
                    "public_metrics": tweet.public_metrics,
                })
        return tweets