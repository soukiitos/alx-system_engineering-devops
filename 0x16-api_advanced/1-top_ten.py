#!/usr/bin/python3
"""
Queries the Reddit API
"""
import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "KiitosUserAgent/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    res_data = response.json().get("data")
    [print(c.get("data").get("title")) for c in res_data.get("children")]
