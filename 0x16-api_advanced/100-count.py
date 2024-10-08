#!/usr/bin/python3
""" Functions to adcquire info from API Reddit"""
import requests
after = None


def count_words(subreddit, word_list):
    """Count the titles found with wordlist in subreddit"""
    my_list = recurse(subreddit)
    my_dict = {}

    if my_list:
        for word in word_list:
            my_dict[word] = 0

        for title in my_list:
            title_split = title.split(" ")

            for iter in title_split:
                for iter_split in word_list:
                    if iter.lower() == iter_split.lower():
                        my_dict[iter_split] += 1

        for key, val in sorted(my_dict.items(),  key=lambda x: x[1],
                               reverse=True):
            if val != 0:
                print("{}: {}".format(key, val))


def recurse(subreddit, hot_list=[]):
    """ recurse is a function that return hot list from
        a subreddit"""
    global after
    headers = {'User-Agent': 'ledbag123'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)
    if response.status_code == 200:
        prox = response.json().get('data').get('after')

        if prox is not None:
            after = prox
            recurse(subreddit, hot_list)
        list_titles = response.json().get('data').get('children')

        for title_ in list_titles:
            hot_list.append(title_.get('data').get('title'))
        return hot_list
    else:
        return (None)

