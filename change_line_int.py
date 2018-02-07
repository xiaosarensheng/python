#!/usr/bin/python
#-*- coding: UTF-8 -*-

import re
import sys
file = open("abcd1.txt","r")
lines = file.readlines()
file = open("abcd1.txt","w")
l_list = lines[:]
for la in l_list:
        if la.find('spec') == -1:
            v = ''
        else:
            v = la
        file.write(v)
file.close()


