#coding:utf-8
import md5
import requests
import json
import time
import random
from config.config_data import *

#字符串md5加密
def get_md5(need_str):
    md = md5.new()
    md.update(need_str)
    return md.hexdigest()

#处理get和post请求并返回请求结果
def requests_result(method, url = '', body = '', headers = '', verify = False):
    if method not in ('get','post'):
        print "暂未配置get以及post外的方法".decode('utf-8')
        return 0
    elif url == '':
        print "未配置url,请配置后使用".decode('utf-8')
    elif method == 'get':
        RST = requests.get(url)
        return RST.text
    elif method == 'post':
        if body == '' and headers == '':
            RST = requests.post(url, verify = verify)
        elif body != '' and headers == '':
            RST = requests.post(url, data = body, verify = verify)
        elif body != '' and headers != '':
            RST = requests.post(url, data = body, headers = headers, verify = verify)
        return RST.text


#处理字符串为json格式
def result_to_json(result_str, array_need = []):
    RST = ''
    try:
        RST = json.loads(result_str)
    except:
        try:
            #处理可能包含在()内的json字符串
            temp_str = result_str.split('(')[1].split(')')[0]
            RST = json.loads(temp_str)
        except:
            print "字符串处理json失败".decode('utf-8')
            return 0
            
    temp = len(array_need)
    if temp == 0:
        print "未提供需求字段".decode('utf-8')
    else:
        return_json = {}
        for i in range(0, temp):
            try:
                if array_need[i] in RST.keys():
                    return_json[array_need[i]] = RST[array_need[i]]
                else:
                    return_json[array_need[i]] = ''
            except:
                print "提供需求字段错误".decode('utf-8')
        return return_json   


#打印分界线
def get_split_line():
    print '---------------------------------------------------------------------'


#等待时间
def wait_time(maxtime, mintime = time_config['mintime']):
    sleep_time = random.randint(mintime, maxtime)
    print '等待'.decode('utf-8'),sleep_time,'s'
    time.sleep(sleep_time)


#设置hosts
def modify_hosts():
    fp = open(r"C:\Windows\System32\drivers\etc\hosts", 'w')
    fp.write(hosts_config)
    fp.close()
    print 'Hosts设置成功'.decode('utf-8')



