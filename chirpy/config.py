# chirpy.config
# Uses confire to get meaningful configurations from a yaml file
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Fri Sep 19 11:14:33 2014 -0400
#
# For license information, see LICENSE.txt
#
# ID: config.py [] benjamin@bengfort.com $

"""
Uses confire to get meaningful configurations from a yaml file
"""

##########################################################################
## Imports
##########################################################################

import os
import confire

##########################################################################
## Constants
##########################################################################

PROJECT_DIR  = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FIXTURES_DIR = os.path.join(PROJECT_DIR, "fixtures")

##########################################################################
## Configuration
##########################################################################

class ChirpyConfiguration(confire.Configuration):
    """
    Meaningful defaults and required configurations.

    debug:    the app will print or log debug statements
    testing:  the app will not overwrite important resources
    api_key:  connection information for mongo
    """

    CONF_PATHS = [
        "/etc/chirpy.yaml",                      # System configuration
        os.path.expanduser("~/.chirpy.yaml"),    # User specific config
        os.path.abspath("conf/chirpy.yaml"),     # Local configuration
    ]

    debug    = True
    testing  = True
    api_key  = None
    fixtures = FIXTURES_DIR

## Load settings immediately for import
settings = ChirpyConfiguration.load()

if __name__ == '__main__':
    print settings
