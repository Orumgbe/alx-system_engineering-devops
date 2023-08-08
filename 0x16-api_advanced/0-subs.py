#!/usr/bin/python3
"""Query reddit api to get number of subscribers for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Returns number of subscribers to the subreddit"""
    url = "http://api.reddit.com/r/{}/about".format(subreddit)
    header = {"User-Agent": "/u/k4rma_sutra"}
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
