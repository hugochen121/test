#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-----------------------------------------
     * * * Angeles Motors Inc. * * *
-----------------------------------------

Created on Tue Jun  9 10:41:55 2020

@author: bianhungchen

Source:
    
Function:
    
"""



import unittest
import test_usb

class testingusb(unittest.TestCase):
    
    # def setUpClass(self):
    #     self.usb_info = test_usb.get_usb_info() # for example

    
    def test_info(self):
        usb_info = test_usb.get_usb_info() # for example
        
        self.assertEqual(test_usb.get_usb_info(), usb_info )

    # def tearDownClass(self):
    #     print('done')


if __name__ == '__main__':
    unittest.main()
    


    


    


    


