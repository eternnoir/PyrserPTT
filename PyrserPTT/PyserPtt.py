#! /usr/bin/env python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
from PyrserPTT import Artical, PttHtmlGraber

pttSiteUrl = 'http://www.ptt.cc'
pttUrlTmp = pttSiteUrl+'/bbs/{0}/'

class PyserPtt(object):

    listMaxLength = 30

    def __init__(self, board,pages=1):
        self._board = board
        self._url = pttUrlTmp.format(board)+'index.html'
        self._pages = pages
        self._graber = PttHtmlGraber.WebPttBot(board)

    def parserHtmltoArtical(self,url=None):
        if url is None:
            url = self._url
        html = self._graber.getHtmlContent(url)
        soup = BeautifulSoup(html)
        articalList = []
        for articalset in soup.findAll('div', attrs={'class': 'r-ent'}):
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

                # print html
                a = Artical.Artical(
                    title=Title,
                    nrec=Nrec,
                    url=Url,
                    mark=Mark,
                    date=Date,
                    author=Author,
                    board=self._board)
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
            print priUrl
            retList.extend(self.parserHtmltoArtical(priUrl))
            priUrl = pttSiteUrl+self._getPriUrl(priUrl)
        return retList

    def _getPriUrl(self,currentUrl):
        html = self._graber.getHtmlContent(currentUrl)
        print currentUrl
        soup = BeautifulSoup(html)
        for link in soup.findAll('a',href=True):
            if u'上頁' in link.text:
                return link['href']

