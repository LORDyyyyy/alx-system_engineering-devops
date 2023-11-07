#!/usr/bin/python3
""" """
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """ """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subs = data['data']['subscribers']
        return (subs)
    else:
        return (0)
