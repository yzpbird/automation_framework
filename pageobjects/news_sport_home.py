#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
  @Time    : 2019/10/16 14:35
  @Author  : yanzhipeng
  @File    : news_sport_home.py
'''

from framework.base_page import BasePage


class SportNewsHomePage(BasePage):
    # NBA入口
    nba_link = "xpath=>//*[@id='channel-submenu']/div/span[2]/a[1]"

    def click_nba_link(self):
        self.click(self.nba_link)
        self.sleep(2)
