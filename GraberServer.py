# -*- coding: utf-8 -*-
__author__ = 'frank'

from PyrserPTT import PyserPtt
from mongoengine import *
import multiprocessing
import time
import hashlib
import sys

connect('admin',host='mongodb://')

boardList = []



def getNewAtricalByBorad(board,pages=2):
    graber = PyserPtt.PyserPtt(board,pages)
    articalList = graber.getArticalList()
    checkAndSaveArtical(articalList)

def checkAndSaveArtical(articalList):
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

def doGrabing():
     while True:
        print 'Grabing.....'
        pool = multiprocessing.Pool(processes=len(boardList))
        for b in boardList:
            pool.apply_async(getNewAtricalByBorad,(b,))
        pool.close()
        pool.join()
        print 'Sleep.....'
        time.sleep(180)

def doUpdateAll():
    urlList = PyserPtt.Artical.Artical.objects().distinct('url')
    print 'Check '+str(len(urlList))+' Urls'
    for url in urlList:
        print 'Update ' + url;
        try:
            checkAndSaveArtical([ _getArticalByUrl(url)])
        except Exception:
            print 'Can not update '+ url
        time.sleep(3)
    return

def _getArticalByUrl(url):
    contentGraber = PyserPtt.PttHtmlGraber.WebPttBot('')
    oldarti = PyserPtt.Artical.Artical.objects(url = url)[0]
    html = contentGraber.getHtmlContent(PyserPtt.pttSiteUrl+url)
    a = PyserPtt.Artical.Artical(
        title=oldarti.title,
        nrec=oldarti.nrec,
        url=oldarti.url,
        mark=oldarti.mark,
        date=oldarti.date,
        author=oldarti.author,
        board=oldarti.board,
        htmlcontent = html)
    return a

if __name__ == "__main__":
    par = None
    if len(sys.argv)>1:
       par = sys.argv[1]
    print par
    if par == 'u':
        doUpdateAll()
    else:
        doGrabing()



