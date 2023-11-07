#!/usr/bin/python3
""" here goes the script"""
import requests
from sys import argv


def top_ten(subreddit):
    """ top ten in a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    user_agent = {'User-agent': 'Google Chrome Version 118.0.5993.120'}
    response = requests.get(url, headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        top = [post['data']['title'] for post in data['data']['children']][:10]
        for i in top:
            print(i)
    else:
        return (None)
