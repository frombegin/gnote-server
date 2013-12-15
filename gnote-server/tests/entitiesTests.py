#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import unittest

from core.entiries import UserInfo

class Test(unittest.TestCase):


    def testUserInfo(self):
        ui = UserInfo()
        ui.name = u"张三"
        ui.email = u"zhang.san@gmail.com"
        self.assertTrue(unicode(ui) == u"张三 <zhang.san@gmail.com>", "")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testUserInfo']
    unittest.main()