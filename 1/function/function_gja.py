#coding:utf-8
from function_common import *


#签到，获取财币
def gxs_sign(member_key):

    url = r'https://u.api.guxiansheng.cn/index.php?c=sign&a=post'
    body = r'appId=android&key=' + member_key['key'] + '&member_id=' + member_key['member_id']
    headers = {
            'Content-Type':r'application/x-www-form-urlencoded; charset=UTF-8'
    }
    requestMethod = 'post'    

    #获取请求结果
    temp_result = requests_result(requestMethod, url, body, headers)
    #处理结果
    sign_result = result_to_json(temp_result, ['code','message','data'])
    if sign_result['code'] == 1:
        #返回data中包含的hashkey
        print 'OK!', sign_result['message'], '获取财币成功!!!'.decode('utf-8')
    else:
        print 'False!', sign_result['data'], '获取财币失败!!!'.decode('utf-8')

#获取hashkey
def get_hashkey(member_key):
    
    #获取HashKey
    url = r'https://trade.api.guxiansheng.cn/index.php?c=buy&a=get&v=2.1'
    body = r'object_id=85&goods_type=1&appId=android&key=' + member_key['key'] + '&member_id=' + member_key['member_id']
    headers = {
            'Content-Type':r'application/x-www-form-urlencoded; charset=UTF-8'
    }
    requestMethod = 'post'

    #获取请求结果
    temp_result = requests_result(requestMethod, url, body, headers)
    #处理结果
    hashkey_result = result_to_json(temp_result, ['code','message','data'])
    #检查code对应的值
    if hashkey_result['code'] == 1:
        #返回data中包含的hashkey
        print 'OK!', hashkey_result['message'], '获取到的hashkey : '.decode('utf-8') + hashkey_result['data']['hashkey']
        return hashkey_result['data']['hashkey']
    else:
        print 'False!', hashkey_result['message'], 'hashkey获取失败!!!'.decode('utf-8')
        return 0
    

#订阅股机A
def handle_GujiA(member_key):

    #签到
    gxs_sign(member_key)
    #获取hashkey
    hashkey = get_hashkey(member_key)
    
    if hashkey != 0:
        #订阅股机A
        url = r'https://trade.api.guxiansheng.cn/index.php?c=buy&a=nb_step2'
        body = r'goods_id=1&hashkey=' + hashkey + '&channel=tengxun&appId=android&key=' + member_key['key'] + '&member_id=' + member_key['member_id']
        headers = {
                'Content-Type':r'application/x-www-form-urlencoded; charset=UTF-8'
        }
        requestMethod = 'post'

        #获取请求结果
        temp_result = requests_result(requestMethod, url, body, headers)
        #处理结果
        GujiA_result = result_to_json(temp_result, ['code','message','data'])                
        #检查code对应的值
        if GujiA_result['code'] == 1:
            print 'OK!', GujiA_result['message'],'股机A订阅成功!!!'.decode('utf-8')
        else:
            print 'False!', GujiA_result['message'],'股机A订阅失败!!!'.decode('utf-8')

