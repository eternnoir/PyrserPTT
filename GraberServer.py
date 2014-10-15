# -*- coding: utf-8 -*-
__author__ = 'frank'

from PyrserPTT import PyserPtt
from mongoengine import *
import multiprocessing
import time
import hashlib

connect('admin',host='mongodb://')

boardList = ['']

def getNewAtricalByBorad(board,pages=2):
    graber = PyserPtt.PyserPtt(board,pages)
    articalList = graber.getArticalList()
    print 'GET ' + str(len(articalList))+'POSTs'
    for a in articalList:
        exits = PyserPtt.Artical.Artical.objects(url = a.url)
        if len(exits) is 0:
            print 'Save '+a.title
            a.save()
        else:
            if isDiffArtical(exits,a):
                a.save()
                print 'Diff '+ a.title
            else:
                print 'NOCHG '+a.title

def isDiffArtical(articalList,newArtical):
    newArtMd5 = getMd5(newArtical.htmlcontent)
    for art in articalList:
        if newArtMd5 == getMd5(art.htmlcontent):
           return False
    return True

def getMd5(ori):
    ori = ori.encode('utf8')
    md5str = hashlib.md5(ori).hexdigest()
    return md5str

if __name__ == "__main__":
    while True:
        print 'Grabing.....'
        pool = multiprocessing.Pool(processes=len(boardList))
        for b in boardList:
            pool.apply_async(getNewAtricalByBorad,(b,))
        pool.close()
        pool.join()
        print 'Sleep.....'
        time.sleep(180)


