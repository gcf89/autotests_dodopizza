#!/usr/bin/python

import os
import unittest
from selenium import webdriver

class RunTest(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(30)
    self.driver.maximize_window()

    self.driver.get("http://dodopizza.ru")


  def test_stub(self):
    return True


  def tearDown(self):
    self.driver.quit()

if __name__ == '__main__':
  unittest.main(verbosity=2)

