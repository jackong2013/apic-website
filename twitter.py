import requests

r = requests.get("https://api.twitter.com/1.1/search/tweets.json?q=%40twitterapi")

print r