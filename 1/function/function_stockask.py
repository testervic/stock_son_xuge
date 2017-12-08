#coding:utf-8
import random
from function_common import *
from function_hq import *

#股问
def stock_ask(member_key, question = question):

    #获取筛选股票
    stock = get_stock(stock_sort)
    #拼装提问内容
    ask_question = random.choice(question['front']).decode('utf-8') + stock['SNAM'] + random.choice(question['end']).decode('utf-8')
    
    url = r'https://u.api.guxiansheng.cn/index.php?c=question&a=post'
    body = {
            'stock_code':stock['FCOD'],
            'stock_name' : stock['SNAM'],
            'intro' : ask_question,
            'appId' : 'android',
            'key' : member_key['key'],
            'member_id' : member_key['member_id']
        }
    headers = {
            'Content-Type':r'application/x-www-form-urlencoded; charset=UTF-8'
    }
    requestMethod = 'post'    

    #获取请求结果
    temp_result = requests_result(requestMethod, url, body, headers)
    #处理结果
    stock_ask_result = result_to_json(temp_result, ['code','message','data'])
    if stock_ask_result['code'] == 1:        
        print 'OK!', stock_ask_result['message'], '股问成功!!! 提问内容：'.decode('utf-8') + ask_question
    else:
        print 'False!', stock_ask_result['message'], '股问失败!!!'.decode('utf-8')
    
