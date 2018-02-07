#!/usr/bin/python
#-*- coding: UTF-8 -*-

import re
import os
import sys
import glob


pwd = os.getcwd()
pwd_sig = glob.glob('./sig/*.txt')
print pwd
print pwd_sig
for index_pwd_sig in pwd_sig:
    file = open(index_pwd_sig)
    lines = file.readlines()

    file = open(index_pwd_sig,"w")

    l_list = lines[:]
    for la in l_list:
        if la.find('rule_type') == -1:
            v = la
        else:
            v =  "  rule_set: ALL\n" + la
        file.write(v)
file.close()

pwd_spec = glob.glob('*.spec')
for index_pwd_spec in pwd_spec:
    file_spec = open(index_pwd_spec)
    lines_spec = file_spec.readlines()

    file_spec = open(index_pwd_spec,"w")

    l_list_spec = lines_spec[:]
    for lb in l_list_spec:
        if lb.find('popularity') == -1:
            x = lb
        else:
            x =  "  rule_set: ALL\n" + lb
        file_spec.write(x)
file.close()