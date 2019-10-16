#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
  @Time    : 2019/10/16 14:34
  @Author  : yanzhipeng
  @File    : baidu_news_home.py
'''

from framework.base_page import BasePage

class NewsHomePage(BasePage):

    #体育新闻入口
    sports_link = "xpath=>//*[@id='channel-all']/div/ul/li[5]/a"

    def click_sports(self):
        self.click(self.sports_link)
        self.sleep(2)

