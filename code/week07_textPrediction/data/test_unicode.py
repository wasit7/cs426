# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 01:07:32 2015

@author: Wasit
"""
import codecs

thaiChars=unicode("")
for i in xrange(3585,3675+1):
    thaiChars+=unichr(i)
with codecs.open("uni.txt","w","utf-8-sig") as u:
    u.write(thaiChars)