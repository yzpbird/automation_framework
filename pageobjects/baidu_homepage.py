#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
  @Time    : 2019/10/15 17:28
  @Author  : yanzhipeng
  @File    : baidu_homepage.py
'''

from framework.base_page import BasePage


class HomePage(BasePage):
    input_box = "id=>kw"
    search_submit_btn = "xpath=>//*[@id='su']"

    def type_search(self, text):
        self.type(self.input_box, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)
