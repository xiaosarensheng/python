from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import json
import re
import time
import csv
import codecs
"""
[腾讯软件,购物,阅读,新闻,视频,旅游,工具,社交,音乐,美化,摄影,理财,系统,生活,出行,安全,教育,健康,娱乐,儿童,办公,通讯]
[-10,122,102,110,103,108,115,106,101,119,104,114,117,107,112,118,111,109,105,100,113,116]
"""
articles = []
def get_page_index(categoryId,pageContext):
    obj = {
        'orgame': 1,
        'categoryId': categoryId,
        'pageSize': 20,
        'pageContext': pageContext
    }
    url = 'http://sj.qq.com/myapp/cate/appList.htm?' + urlencode(obj)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引页出错')
        return None

def parse_page_index(html):
    try:
        obj = json.loads(html)
        if obj and 'obj' in obj.keys():
            for item in obj.get('obj'):
                yield item.get('pkgName')
    except:
        parse_page_index(html)

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    Soup = BeautifulSoup(html, 'html.parser')
    app_name = Soup.find(attrs={"class": "det-name-int"}).string
    app_version = Soup.find(attrs={"class": "det-othinfo-data"}).string
    app_time_one =  Soup.find(id=re.compile('J_ApkPublishTime')).get('data-apkpublishtime')
    app_time_two = time.localtime(int(app_time_one))
    #app_time = time.strftime("%Y-%m-%d %H:%M:%S", app_time_two)
    app_time = time.strftime("%Y-%m-%d", app_time_two)
    #application = ["app_name : " + app_name, "app_version : " + app_version, "app_time : " + app_time]
    application = [app_time,app_name,app_version]
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(str(application) + '\n')

    # with open('result1.txt','a',encoding='utf-8') as f:
    #     f.write(str(app_time) + '\n')
    # with open('result2.txt','a',encoding='utf-8') as f:
    #     f.write(str(app_name) + '\n')
    # with open('result3.txt','a',encoding='utf-8') as f:
    #     f.write(str(app_version) + '\n')
    app_time_csv = []
    app_name_csv = []
    app_version_csv = []
    app_time_csv.append(app_time)
    app_name_csv.append(app_name)
    app_version_csv.append(app_version)
    print(app_name_csv)
    with open("test.csv", "a") as csv_file:
        writer = csv.writer(csv_file)
        #writer.writerow(('更新时间','应用名称','软件版本'))
        writer.writerows(zip(app_time_csv, app_name_csv,app_version_csv))

def main(categoryId,pageContext):
    html = get_page_index(categoryId,pageContext)
    for url in parse_page_index(html):
        url = 'http://sj.qq.com/myapp/detail.htm?apkName=' + url
        html = get_one_page(url)
        try:
            parse_one_page(html)
        except:
            main(categoryId,pageContext)

if __name__ == '__main__':
    list = {'top1~20':'undefined', 'top21~40':20, 'top41~60':40}
    #name = [-10, 122, 102, 110, 103, 108, 115, 106, 101, 119, 104, 114, 117, 107, 112, 118, 111, 109, 105, 100, 113, 116]
    #app_cn = ['腾讯软件', '购物', '阅读', '新闻', '视频', '旅游', '工具', '社交', '音乐', '美化', '摄影', '理财', '系统', '生活', '出行', '安全', '教育', '健康', '娱乐', '儿童', '办公', '通讯']
    app_dict = {'腾讯软件':-10, '购物':122, '阅读':102, '新闻':110, '视频':103, '旅游':108, '工具':115, '社交':106, '音乐':101, '美化':119, '摄影':104, '理财':114, '系统':117, '生活':107, '出行':112, '安全':118, '教育':111, '健康':109, '娱乐':105, '儿童':100, '办公':113, '通讯':116}

    for i in app_dict:
        for j in list:
            with open('result.txt', 'a', encoding='utf-8') as f:
                f.write(i + '类应用' + j + '\n')
            main(app_dict[i],list[j])