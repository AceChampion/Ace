#/usr/bin/env python3

import easygui as g
import json
import re
import urllib.request
import urllib.parse
import sys



def translate():
    url = 'http://fanyi.youdao.com/openapi.do'
    key = '695028818'
    keyfrom = 'nicomochina'
    words = g.enterbox('type the word u wanto translate', title = 'tras')
    try:
        url1 = url + '?keyfrom=' + keyfrom + '&key='+key + '&type=data&doctype=json&version=1.1&q=' + urllib.parse.quote(words)
    except:
        return 1
    
    page = urllib.request.urlopen(url1)
    result = page.read().decode('utf-8', 'ignore')
    json_result = json.loads(result)
    json_result = json_result["translation"] 
    g.msgbox(json_result)

while 1:
    if translate():
        sys.exit(0)
