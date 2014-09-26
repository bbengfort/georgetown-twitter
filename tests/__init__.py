# tests
# Testing for the chirpy package
#
# Author:   Benjamin Bengfort <bb830@georgetown.edu>
# Created:  Thu Mar 27 16:49:40 2014 -0400
#
# Copyright (C) 2014 Georgetown University
# For license information, see LICENSE.txt
#
# ID: __init__.py [] bb830@georgetown.edu $

"""
Testing for the chirpy package
"""

##########################################################################
## Imports
##########################################################################

import os
import unittest

##########################################################################
## TestCases
##########################################################################

class InitializationTest(unittest.TestCase):

    def test_initialization(self):
        """
        Test a simple world fact to kick off testing
        """
        self.assertEqual(2**3, 8)

    def test_import(self):
        """
        We are able to import our packages
        """
        try:
            import chirpy
        except ImportError:
            self.fail("Unable to import the chirpy module!")
