#!/usr/bin/python3
import requests

def top_ten(subreddit):
    headers = {'User-Agent': 'MyBot/1.0'}
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except:
        print(None)
