#!/usr/bin/python3
"""
Queries the Reddit API
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
    Return a list containing the titles
    of all hot articles for a given subreddit
    """
    global after
    headers = {"User-Agent": "KiitosUserAgent/1.0"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after}
    response = requests.get(
            url, params=params, headers=headers, allow_redirects=False
            )
    if response.status_code == 200:
        aft_er = response.json().get("data").get("after")
        if aft_er is not None:
            after = aft_er
            recurse(subreddit, hot_list)
        ti_tles = response.json().get("data").get("children")
        for data_title in ti_tles:
            hot_list.append(data_title.get("data").get("title"))
        return hot_list
    else:
        return (None)
