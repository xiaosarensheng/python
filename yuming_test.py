#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import re
import sys
import shutil

def get_new_app_sig():
    file = open("abcd1.txt","r",encoding='utf-8')
    lines = file.readlines()
    l_list = lines[:]
    for la in l_list:
        path_split = la.strip("\x0d\x0a\x09\x20").split('/',-1)
        sig_path = '/'.join(path_split[:-1]) + "/sig"
        app_en = path_split[-1]
        files = os.listdir(sig_path)[0]
        old_sig = sig_path + '/' + files
        app_sig = sig_path + '/' + app_en + "_NewBrowse1111_HTTP_M.txt"
        shutil.copy(old_sig, app_sig)
        yield app_sig
    file.close()
    
def change_value():
    for app_sig in get_new_app_sig():
        app_sig_split = app_sig.split('/')[-1]
        file = open(app_sig,"r",encoding='utf-8')
        lines = file.readlines()
        file.close()
        file = open(app_sig, "w",encoding='utf-8')
        l_list = lines[:]
        for la in l_list:
            if la.find('priority') != -1:
                res = re.findall(r"\d+\.?\d*", la)
                v = re.sub(res[0], str(5+int(res[0])), la)
            elif la.find('    en: ') != -1:
                v = '    en: ' + app_sig_split + '\n'
            elif la.find('    cn: ') != -1:
                v = '    cn: ' + app_sig.split('/')[-3] + "新浏览1111HTTP消息流" + '\n'
            elif la.find('          position: ') != -1:
                l_add4 = ['          position: subheader','          header_name: Host','      -','        content:','          pattern: ',
                   '            - .htm','          position: http_uri']
                for lb in l_add4:
                    v = lb+'\n'
                    file.write(v)
                break
            else:
                v = la
            file.write(v)
        file.close()
        
if __name__ == '__main__':
    change_value()