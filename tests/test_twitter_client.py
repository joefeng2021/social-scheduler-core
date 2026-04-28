"""Tests for Twitter client."""
import pytest
from social_scheduler_core.twitter_client import TwitterClient

def test_client_initialization():
    """Test that client requires bearer token."""
    with pytest.raises(ValueError):
        TwitterClient()