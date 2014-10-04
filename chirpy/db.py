# chirpy.db
# Provides access tools to the database
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Fri Oct 03 23:32:21 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: db.py [] benjamin@bengfort.com $

"""
Provides access tools to the database
"""

##########################################################################
## Imports
##########################################################################

from pymongo import MongoClient
from chirpy.config import settings

##########################################################################
## Helper functions
##########################################################################

def connect(**kwargs):
    defaults = {
        'host': settings.mongo.get('host'),
        'port': settings.mongo.get('port')
    }
    defaults.update(kwargs)
    client = MongoClient(**defaults)
    return client[settings.mongo.database]

if __name__ == '__main__':
    db = connect()
    db.tweets.count()
