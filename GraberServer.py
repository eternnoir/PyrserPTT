# -*- coding: utf-8 -*-
__author__ = 'frank'

from PyrserPTT import PyserPtt
from mongoengine import *
import time

connect('admin',host='')

graber = PyserPtt.PyserPtt('Gossiping',2)
articalList = graber.getArticalList()
while True:
    for a in articalList:
        exits = PyserPtt.Artical.Artical.objects(url = a.url)
        if len(exits) is 0:
            print 'Save '+a.title
            a.save()
        else:
            print 'Exits '+a.title
    time.sleep(10)
