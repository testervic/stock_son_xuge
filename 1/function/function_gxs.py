#coding:utf-8
from function_common import *


#登录，获取用户member_id和最新key
def get_key(teacher_info):

    #登录接口配置
    url = r'https://login.api.guxiansheng.cn/index.php?c=user&a=login'
    body = r'username=' + teacher_info["teacher_mobile"] + r'&password=' + get_md5(teacher_info["teacher_pw"])
    headers = {
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
    }
    requestMethod = 'post'

    return_result = {}

    #获取请求结果
    temp_result = requests_result(requestMethod, url, body, headers)

    #处理结果
    handle_temp_result = result_to_json(temp_result, ['code','message','data'])
    #检查code对应的值
    if handle_temp_result['code'] == 1:
        #返回data中包含的key
        return_result['member_id'] = handle_temp_result['data']['member_id']
        return_result['key'] = handle_temp_result['data']['key']
        print 'OK!', 'member_id和key获取成功!'.decode('utf-8')
        return return_result
    else:
        #返回message
        print 'Fail', handle_temp_result['message']
        return 0
