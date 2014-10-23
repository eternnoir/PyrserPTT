#! /usr/bin/env python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
from PyrserPTT import Artical, PttHtmlGraber
import time

pttSiteUrl = 'http://www.ptt.cc'
pttUrlTmp = pttSiteUrl+'/bbs/{0}/'

class PyserPtt(object):

    def __init__(self, board,pages=1,intervalSec = 1,fromPage=0):
        self._board = board
        self._url = pttUrlTmp.format(board)+'index.html'
        self._pages = pages+fromPage
        self._fromPage = fromPage
        self._graber = PttHtmlGraber.WebPttBot(board)
        self._intervalSec = intervalSec

    def parserHtmltoArtical(self,url=None):
        if url is None:
            url = self._url
        html = self._graber.getHtmlContent(url)
        soup = BeautifulSoup(html)
        articalList = []
        for articalset in soup.findAll('div', attrs={'class': 'r-ent'}):
            time.sleep(self._intervalSec)
            try:
                if articalset.find('span') is not None:
                    Nrec = str(articalset.find('span').text)
                else:
                    Nrec = '0'
                titleset = articalset.find('div', attrs={'class': 'title'})
                Url = titleset.find('a')['href']
                Title = titleset.text
                Mark = articalset.find('div', attrs={'class': 'mark'}).text
                Author = articalset.find('div', attrs={'class': 'author'}).text
                Date = articalset.find('div', attrs={'class': 'date'}).text
                AHtml = self._graber.getHtmlContent(pttSiteUrl+Url)

                # print html
                a = Artical.Artical(
                    title=Title,
                    nrec=Nrec,
                    url=Url,
                    mark=Mark,
                    date=Date,
                    author=Author,
                    board=self._board,
                    htmlcontent = AHtml)
                articalList.append(a)

            except Exception as e:
                print str(e)
                continue
        return articalList

    def start(self):
        self._graber.getHtmlContent()

    def getArticalList(self):
        retList = []
        priUrl = self._url
        for i in range(self._pages):
            if i < self._fromPage:
                priUrl = pttSiteUrl+self._getPriUrl(priUrl)
                continue
            print priUrl
            retList.extend(self.parserHtmltoArtical(priUrl))
        return retList

    def _getPriUrl(self,currentUrl):
        html = self._graber.getHtmlContent(currentUrl)
        print currentUrl
        soup = BeautifulSoup(html)
        for link in soup.findAll('a',href=True):
            if u'上頁' in link.text:
                return link['href']

