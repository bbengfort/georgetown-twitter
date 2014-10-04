# chirpy.twitter
# Wraps Twython to make calls to Twitter
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Fri Sep 26 17:47:01 2014 -0400
#
# For license information, see LICENSE.txt
#
# ID: twitter.py [] benjamin@bengfort.com $

"""
Wraps Twython to make calls to Twitter
"""

##########################################################################
## Imports
##########################################################################

import os
import json

from chirpy.config import settings
from twython import Twython
from datetime import datetime

##########################################################################
## TwitterClient
##########################################################################

class TwitterClient(object):
    """
    Handles the routine of accessing data from Twitter
    """

    def __init__(self, api_key=None, api_secret=None):
        self.appkey  = api_key or settings.get('api_key', None)
        self.secret  = api_secret or settings.get('api_secret', None)
        self.token   = self.get_access_token()
        self.twitter = Twython(self.appkey, access_token=self.token)

    def get_access_token(self):
        twitter = Twython(self.appkey, self.secret, oauth_version=2)
        return twitter.obtain_access_token()

    def search(self, query, **kwargs):
        """
        Executes a Twitter search
        """
        return self.twitter.search(q=query, **kwargs)

    def ingest(self, query, **kwargs):
        """
        Executes a twitter search and saves it to disk, returns the number
        of Tweets that were fetched with the API.
        """
        data = self.search(query, **kwargs)
        name = "%s-%s.json" % (query.replace(" ", "_"), datetime.now().strftime("%Y%m%dT%H%M%S"))
        path = os.path.join(settings.get('fixtures'), name)
        with open(path, 'w') as f:
            json.dump(data, f)

        return data["search_metadata"]["count"]

if __name__ == '__main__':
    client = TwitterClient()
    tweets = client.ingest('python programming')
    print "fetched %i tweets" % tweets
