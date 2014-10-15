# -*- coding: utf-8 -*-
__author__ = 'frank'

from PyrserPTT import PyserPtt
from mongoengine import *
import multiprocessing
import time

connect('admin',host='')

boardList = ['Gossiping']

def getNewAtricalByBorad(board,pages=2):
    graber = PyserPtt.PyserPtt(board,pages)
    articalList = graber.getArticalList()
    for a in articalList:
       exits = PyserPtt.Artical.Artical.objects(url = a.url)
       if len(exits) is 0:
           print 'Save '+a.title
           a.save()
       else:
           print 'Exits '+a.title

if __name__ == "__main__":
    while True:
        pool = multiprocessing.Pool(processes=len(boardList))
        for b in boardList:
            pool.apply_async(getNewAtricalByBorad,(b,))
        pool.close()
        pool.join()
        time.sleep(180)


