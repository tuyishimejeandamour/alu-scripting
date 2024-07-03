#!/usr/bin/python3

import requests

"""
This script returns the number of subscribers for a given subreddit.
"""

def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers.

    Raises:
        ValueError: If the subreddit is not found or an error occurs.

    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            return data.get('subscribers')
        else:
            raise ValueError("Subreddit not found")
    else:
        raise ValueError("An error occurred")
