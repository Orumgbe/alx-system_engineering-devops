#!/usr/bin/python3
"""List of title of all hot articles in given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Queries subreddit for hottest articles"""
    url = 'https://api.reddit.com/r/{}/hot?after={}'.format(subreddit, after)
    agent = {'User-Agent': '/u/k4rma_sutra'}
    res = requests.get(url,  headers=agent)
    h_list = []
    if res.status_code == 200:
        hottest = res.json()["data"]["children"]
        after = res.json()["data"]["after"]

        if after is None:
            h_list = append_page(hottest, len(hottest))
            return h_list
        h_list.append(recurse(subreddit, h_list, after=after))
        h_list = append_page(hottest, len(hottest))
    else:
        return None
    return h_list


def append_page(h_list, count, new_hlist=[]):
    """append each data in the page"""
    if count == 0:
        return new_hlist
    new_hlist.append(h_list[count - 1]["data"]["title"])
    return (append_page(h_list, count - 1, new_hlist))
