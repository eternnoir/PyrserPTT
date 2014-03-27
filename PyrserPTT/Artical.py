#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'frankwang'

class Artical(object):

    title = None
    author= None
    url= None
    date= None
    nrec= None
    mark= None
    htmlcontent= None

    def __init__(self,Tital,Author,Url,Date,Nrec,Mark,Html):
       self.title = Tital

       self.author = Author
       self.url = Url
       self.date = Date
       self.mark = Mark
       self.nrec = Nrec
       self.htmlcontent = Html

