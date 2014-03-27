#! /usr/bin/env python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
from PyrserPTT import Artical, PttHtmlGraber


class PyserPtt(object):

    mainArticalList = []
    listMaxLength = 30
    def __init__(self,board,sleeptime):
        self._board = board
        self._sleepTime = sleeptime
        self._graber = PttHtmlGraber.WebPttBot(board)

    def parserHtmltoArtical(self):
        html = self._graber.getHtmlContent()
        soup = BeautifulSoup(html)
        articalList = []
        for articalset in soup.findAll('div', attrs={'class': 'r-ent'}):
            try:
                if articalset.find('span') is not None:
                    Nrec = str(articalset.find('span').text)
                else:
                    Nrec = '0'
                titleset=  articalset.find('div',attrs={'class':'title'})
                Url = titleset.find('a')['href']
                Title = titleset.text
                Mark =  articalset.find('div',attrs={'class':'mark'}).text
                Author =  articalset.find('div',attrs={'class':'author'}).text
                Date =  articalset.find('div',attrs={'class':'date'}).text
                self._graber.getBrowser().open(Url)
                Html = self._graber.getBrowser().response().read()
                #print html
                a = Artical.Artical(title=Title,nrec=Nrec,url=Url,mark=Mark,
                                    date=Date,author=Author,htmlcontent=Html,board=self._board)
                articalList.append(a)

            except Exception,e:
                print str(e)
                continue
        return articalList


    def start(self):
        self._graber.getHtmlContent()

    def getNewArticals(self):
        nowList = self.parserHtmltoArtical()
        returnList = []
        for na in nowList:
            isContain = False
            for aa in self.mainArticalList:
                if na.url == aa.url:
                    isContain = True
            if len(self.mainArticalList)>self.listMaxLength:
                print 'del frome list'
                self.mainArticalList.pop(0)

            if isContain is False:
                self.mainArticalList.append(na)
                returnList.append(na)

        return returnList







