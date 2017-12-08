#coding:utf-8
import random
from function_common import *
from config.config_data import *

#获取股票和股票代码
def get_stock(stock_sort):

    pageNo = stock_sort['pageNo']
    pageSize = stock_sort['pageSize']
    sortField = stock_sort['sortField']
    
    #行情个股排行，构建url
    url = r'http://mk2.api.guxiansheng.cn/?mod=quote&a=get&c=stk_sort&pageNo=' +  pageNo + '&pageSize=' + pageSize + '&sortField=' + sortField
    requestMethod = 'get'

    #获取请求结果
    temp_result = requests_result(requestMethod, url)

    #处理结果
    handle_temp_result = result_to_json(temp_result, ['data'])

    #返回的结果
    return_result = {}

    #该接口返回只包含data,无code
    if len(handle_temp_result) == 0:
        print "无符合条件的个股".decode('utf-8')
        return 0
    else:
        stock_info = random.choice(handle_temp_result['data'])
        return_result['SNAM'] = stock_info['SNAM']
        return_result['FCOD'] = stock_info['FCOD']
        return return_result
        
