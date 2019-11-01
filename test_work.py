#!/usr/bin/python

import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class RunTest(unittest.TestCase):

  def setUp(self):
    self.d = webdriver.Chrome()
    self.d.maximize_window()

    self.d.get("http://dodopizza.ru")


  def test_popup(self):
    # popup_dialog = self.d.find_element_by_class_name('popup_dialog-inner')
    # self.assertTrue(popup_dialog.is_displayed())

    WebDriverWait(self.d, 5)\
      .until(expected_conditions.visibility_of_element_located(\
          (By.CLASS_NAME, "popup__dialog-inner")))

    popup_logo = self.d.find_element_by_class_name('locality-selector-popup__logo')
    self.assertTrue(popup_logo.is_displayed())

    # todo: check dodo logo is what you need

    popup_search = self.d.find_element_by_class_name('locality-selector-popup__search')
    self.assertTrue(popup_search.is_displayed())

    # todo: input by xpath or ?

  def tearDown(self):
    self.d.quit()

if __name__ == '__main__':
  unittest.main(verbosity=2)

