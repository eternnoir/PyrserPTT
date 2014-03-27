#! /usr/bin/env python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
from PyrserPTT import Artical, PttHtmlGraber


class PyserPtt(object):

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
                    nrec = str(articalset.find('span').text)
                else:
                    nrec = '0'
                titleset=  articalset.find('div',attrs={'class':'title'})
                url = titleset.find('a')['href']
                title = titleset.text
                mark =  articalset.find('div',attrs={'class':'mark'}).text
                author =  articalset.find('div',attrs={'class':'author'}).text
                date =  articalset.find('div',attrs={'class':'date'}).text
                #self._graber.getBrowser().open(url)
                #html = self._graber.getBrowser().response().read()
                #print html
                a = Artical.Artical(title,author,url,date,nrec,mark,'')
                articalList.append(a)

            except:
                print "error"
                continue
        return articalList


    def start(self):
        self._graber.getHtmlContent()




