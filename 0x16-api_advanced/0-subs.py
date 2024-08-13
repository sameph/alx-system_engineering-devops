#!/usr/bin/python3
""" Exporting csv files"""
import requests


def number_of_subscribers(subreddit):
    """Read reddit API and return number subscribers """
    headers = {'user-agent': '/u/alx_advanced_API'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False)
    if r.status_code == 200:
        return (r.json()["data"]["subscribers"])
    else:
        return(0)
