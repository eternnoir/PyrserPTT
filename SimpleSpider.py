#! /usr/bin/env python
# -*- coding: utf-8 -*-


from mongoengine import *
from PyrserPTT import PyserPtt
import time
import random

__author__ = 'frankwang'


connect('ptt',host='')

class SimplePTTSpider(object):
    def __init__(self,board):
        self._parser = PyserPtt.PyserPtt(board,5)

    def Start(self):
        while 1:
            print 'parser start'
            try:
                for arti in self._parser.getNewArticals():
                    msg = str(arti.nrec).ljust(2)+' '+arti.mark+' '+str(arti.author).ljust(13)\
                          +str(arti.date).ljust(6)+arti.title+'    < http://www.ptt.cc'+arti.url+' >'
                    arti.save()
                    id = arti.id
                    print id
                    print msg
                    time.sleep(3)
            except Exception,e:
                print str(e)
            time.sleep(random.randint(5,50))


