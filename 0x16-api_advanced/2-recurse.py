#!/usr/bin/python3
"""List of title of all hot articles in given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns list of titles of hot articles in subreddit"""
    url = "http://api.reddit.com/r/{}/hot?after={}".format(subreddit, after)
    header = {
        "User-Agent": "/u/k4rma_sutra"
    }
    r = requests.get(url, headers=header)
    if r.status_code != 200:
        print(r.status_code)
        return None

    listings = r.json()['data']['children']
    for post in listings:
        hot_list.append(post['data']['title'])
    after = r.json()['data']['after']
    if after is not None:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
