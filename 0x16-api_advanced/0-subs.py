#!/usr/bin/python3
"""
Queries the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    '''Return the number of subscribers for a given subredit'''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "KiitosUserAgent/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    res_data = response.json().get("data")
    return res_data.get("subscribers")
