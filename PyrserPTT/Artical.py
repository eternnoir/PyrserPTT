#! /usr/bin/env python
# -*- coding: utf-8 -*-
from mongoengine import *
import datetime

__author__ = 'frankwang'


class Artical(Document):

    title = StringField(required=True)
    board = StringField(required=True)
    author= StringField()
    url= StringField()
    date= StringField()
    nrec= StringField()
    mark= StringField()
    updateDate = DateTimeField(default=datetime.datetime.now)
    htmlcontent= StringField()


