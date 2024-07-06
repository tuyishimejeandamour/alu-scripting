#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'MyBot/1.0'}
    
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except:
        return 0
