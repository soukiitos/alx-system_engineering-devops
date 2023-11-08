#!/usr/bin/python3
"""
Queries the Reddit API
"""
import requests


def count_words(subreddit, word_list, after="", words_count=[]):
    """
    Parses the title of all hot articles,
    and prints a sorted count of given keywords
    """
    if after == "":
        words_count = [0] * len(word_list)
    headers = {"User-Agent": "KiitosUserAgent/1.0"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    response = requests.get(
            url, params=params, headers=headers, allow_redirects=False
            )
    if response.status_code == 200:
        data = response.json()
        for da_ta in (data['data']['children']):
            for word in da_ta['data']['title'].split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        words_count[i] += 1
        after = data['data']['after']
        if after is None:
            save = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        save.append(j)
                        words_count[i] += words_count[j]
            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (
                            words_count[j] > words_count[i] or
                            (word_list[i] > word_list[j] and
                                words_count[j] == words_count[i])
                            ):
                        da_ta = words_count[i]
                        words_count[i] = words_count[j]
                        words_count[j] = da_ta
                        da_ta = word_list[i]
                        word_list[i] = word_list[j]
                        word_list[j] = da_ta
            for i in range(len(word_list)):
                if (words_count[i] > 0) and i not in save:
                    print("{}: {}".format(
                        word_list[i].lower(), words_count[i])
                        )
        else:
            count_words(subreddit, word_list, after, words_count)
