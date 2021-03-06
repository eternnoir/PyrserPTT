#! /usr/bin/env python
# -*- coding: utf-8 -*-

import cookielib
import sys
import urllib

from BeautifulSoup import BeautifulSoup
import mechanize


class WebPttBot(object):

    def __init__(self,board):
        self._board = board
        # Browser
        self._br = mechanize.Browser()

        # Cookie Jar
        cj = cookielib.LWPCookieJar()
        self._br.set_cookiejar(cj)

        # Browser options
        self._br.set_handle_equiv(True)
        self._br.set_handle_redirect(True)
        self._br.set_handle_referer(True)
        self._br.set_handle_robots(False)

        # Follows refresh 0 but not hangs on refresh > 0
        self._br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        # User-Agent (this is cheating, ok?)
        self._br.addheaders = [('User-agent', "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1)"
                                              " Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1")]

    def __checkPage(self):
        response = self._br.open(self._url)
        currentUrl = response.geturl()
        print currentUrl
        if "over18" in currentUrl:
            return self.___confirmOver18()
        else:
           return True

    def ___confirmOver18(self):
        self._br.select_form(nr=0)
        response = self._br.submit()
        url = response.geturl()
        if self._board+'/index.html' in url:
            return True
        else:
            return False

    def getBrowser(self):
        return self._br

    def getHtmlContent(self, url):
        self._url = url
        if self.__checkPage() is True:
            response = self._br.open(self._url)
            return response.read()
        else:
            raise Exception("Can not open target page")

