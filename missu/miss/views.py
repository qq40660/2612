#-*- coding:utf-8 -*-
from django.http import HttpResponse
import requests
import json

qq = ""#myqq 
pmd5 = "" #qq password md5 for tencent
who = "" #add msg for who
bid_code = "qzoneLogin"
go_url = "http://m.qzone.com/profile?"

def login_qzone():
    url = 'http://pt.3g.qq.com/login?act=json&sidtype=0'
    data = {
            "qq":qq,
            "pmd5":pmd5,
            "bid_code":"qzoneLogin",
            "go_url":"http://m.qzone.com/profile?"
        }
    headers = {
            'Host':'pt.3g.qq.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20100101 Firefox/21.0',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer':'http://pt.3g.qq.com/s?aid=newqzone&go_url=http%3A%2F%2Fm.qzone.com%2Fprofile%3F'
        }
    r = requests.post(url=url, data=data, headers=headers)
    return json.loads(r.text)
    
def add_msg(msg):
    
    sid = login_qzone()['sid']
    url = 'http://blog60.z.qq.com/mmsgb/add_msg.jsp?entry=blog&sid=%s'%sid
    data = {
            'msg':msg,
            'sign':'0',
            'B_UID':who,
            'i_p_w':'msg|'
        }

    r = requests.post(url=url, data=data)

def miss(request):
    add_msg(u'早安')
    return HttpResponse('Miss U')

