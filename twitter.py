# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import json
from urllib import quote

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "0oobQRZKPqZugeUfGrWVwK3zT"
CONSUMER_SECRET = "gcXW0FJsOUbvn1Pkec6LE9tqk4WSIjN38O0u6aVg8r26pckFj8"

OAUTH_TOKEN = "355164055-LAEpWGYWDeeVtj7830ODlPP9IA7efaBbVLM1lDde"
OAUTH_TOKEN_SECRET = "lLLaluUuI2YW6PIJ7r9iv1NK7ApSDLqx4qD0liQLH6IWE"


SEARCH_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=chuesaihou'


def setup_oauth():
    """Authorize your app via identifier."""
    # Request token
    oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)

    resource_owner_key = credentials.get('oauth_token')[0]
    resource_owner_secret = credentials.get('oauth_token_secret')[0]

    # Authorize
    authorize_url = AUTHORIZE_URL + resource_owner_key
    print 'Please go here and authorize: ' + authorize_url

    verifier = raw_input('Please input the verifier: ')
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)

    # Finally, Obtain the Access Token
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    token = credentials.get('oauth_token')[0]
    secret = credentials.get('oauth_token_secret')[0]

    return token, secret


def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth


def get_posts():
	oauth = get_oauth()
	r = requests.get(url=SEARCH_URL, auth=oauth)
	print json.dumps(r.json(), sort_keys=True,
                  indent=4, separators=(',', ': '))

get_posts()

# if __name__ == "__main__":
#     if not OAUTH_TOKEN:
#         token, secret = setup_oauth()
#         print "OAUTH_TOKEN: " + token
#         print "OAUTH_TOKEN_SECRET: " + secret
#         print
#     else:
#         oauth = get_oauth()
#         r = requests.get(url="https://api.twitter.com/1.1/statuses/mentions_timeline.json", auth=oauth)
#         print r.json()