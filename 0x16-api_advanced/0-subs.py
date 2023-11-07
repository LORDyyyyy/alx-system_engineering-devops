#!/usr/bin/python3
""" """
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """ """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    user_agent = {'User-agent': 'Google Chrome Version 118.0.5993.120'}
    response = requests.get(url, headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subs = data['data']['subscribers']
        return (subs)
    else:
        return (0)
