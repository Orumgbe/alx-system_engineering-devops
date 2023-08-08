#!/usr/bin/python3
"""Query reddit api for top ten posts in given subreddit"""

import requests


def top_ten(subreddit):
    """Returns first 10 hot posts subreddit"""
    url = "http://api.reddit.com/r/{}/hot".format(subreddit)
    header = {
        "User-Agent": "/u/k4rma_sutra",
        "allow_redirects": "False"
    }
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        listings = r.json()['data']['children']
        count = 0
        for hot in listings:
            print(hot['data']['title'])
            count += 1
            if count == 10:
                break
    else:
        print("None")
