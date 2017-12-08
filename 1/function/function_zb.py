#coding:utf-8
from function_common import *
from config.config_data import *
import random
import time

#获取直播列表
def gxs_zb_list():
    
    url = r'https://clb.api.guxiansheng.cn/index.php?c=policy_new&a=policySellers&v=2.0.1'
    body = r'curpage=1&pagesize=30&keywords=&point=0&seller_type=&sort=&appId=android&key=&member_id=0'
    headers = {
            'Content-Type':r'application/x-www-form-urlencoded; charset=UTF-8'
    }
    requestMethod = 'post'    

    #获取请求结果
    temp_result = requests_result(requestMethod, url, body, headers)
    #处理结果
    stock_ask_result = result_to_json(temp_result, ['code','message','data'])
    
    if stock_ask_result['code'] == 1:        
        print 'OK!', stock_ask_result['message'], '获取直播列表成功!!!'.decode('utf-8')
        return stock_ask_result['data']['list']
    else:
        print 'False!', stock_ask_result['message'], '获取直播列表失败!!!'.decode('utf-8')
        return 0


#确定循环评论次数, 目前最大为3, 返回直播老师ID
def loop_seller_id(num):

    #获取直播列表结果
    get_zb_list = gxs_zb_list()

    #返回seller_id
    return_result = []
    
    if len(get_zb_list) == 0 or get_zb_list == 0:
        print '获取到当前直播列表内容为空'.decode('utf-8')
        return 0
    else:
        #确定循环评论次数
        if len(get_zb_list) > num:
            loop_num = num
        else:
            loop_num = len(get_zb_list)
            
        for i in range(0, loop_num):
            return_result.append(get_zb_list[i]['seller_id'])
        
        return return_result
    


#获取直播间详情, 返回第一条直播policy_id
def gxs_zb_details(seller_id):

    #获取进行评论的老师ID
    url = r'https://clb.api.guxiansheng.cn/index.php?c=policy_new&a=getPolicyList&v=2.0.1'
    body = r'seller_id=' + str(seller_id) + '&is_history_point=0&refresh=0&curpage=1&pagesize=15&appId=android&key=&member_id=0'
    headers = {
            'Content-Type':r'application/x-www-form-urlencoded; charset=UTF-8'
    }
    requestMethod = 'post'    

    #获取请求结果
    temp_result = requests_result(requestMethod, url, body, headers)
    #处理结果
    zb_details_result = result_to_json(temp_result, ['code','message','data'])
    

    if zb_details_result['code'] == 1:        
        print 'OK!', zb_details_result['message'], '获取直播间详情成功!!!'.decode('utf-8')
        #返回当前直播间第一条直播的policy_id
        return zb_details_result['data']['policy_list'][0]['policy_id']
    else:
        print 'False!', zb_details_result['message'], '获取直播间详情失败!!!'.decode('utf-8')
        return 0


#评论
def gxs_zb_comment(member_key, policy_id):

    #随机获取评论内容
    comment_message = random.choice(comment)

    #获取进行评论的老师ID
    url = r'https://u.api.guxiansheng.cn/index.php?c=comment&a=post&v=1.1'
    body = {
        'object_id':policy_id,
        'type':3,
        'message':comment_message,
        'pid':0,
        'appId':'android',
        'key':member_key['key'],
        'member_id':member_key['member_id']
        }
    headers = {
            'Content-Type':r'application/x-www-form-urlencoded; charset=UTF-8'
    }
    requestMethod = 'post'    

    #获取请求结果
    temp_result = requests_result(requestMethod, url, body, headers)
    #处理结果
    zb_comment_result = result_to_json(temp_result, ['code','message','data']) 

    if zb_comment_result['code'] == 1:        
        print 'OK!', zb_comment_result['message'], '评论成功!!! 评论内容为 :'.decode('utf-8') + comment_message.decode('utf-8')
    else:
        print 'False!', zb_comment_result['message'], '评论失败!!!'.decode('utf-8')


#答疑解惑
def answer_question(member_key, seller_id):

    question_info = random.choice(teacher_question)
    
    url = r'https://clb.api.guxiansheng.cn/index.php?c=policy&a=questionsPost&v=1.1'
    body = {
        'seller_id':seller_id,
        'json_stock':'',
        'questions':question_info,
        'answer_type':2,
        'questions_way':2,
        'appId':'android',
        'key':member_key['key'],
        'member_id':member_key['member_id']
        }
    headers = {
            'Content-Type':r'application/x-www-form-urlencoded; charset=UTF-8'
    }
    requestMethod = 'post'    

    #获取请求结果
    temp_result = requests_result(requestMethod, url, body, headers)
    #处理结果
    answer_question_result = result_to_json(temp_result, ['code','message','data']) 

    if answer_question_result['code'] == 1:        
        print 'OK!', answer_question_result['message'], '答疑解惑成功!!! 提问内容为 :'.decode('utf-8') + question_info.decode('utf-8')
    else:
        print 'False!', answer_question_result['message'], '答疑解惑失败!!!'.decode('utf-8')
    

#直播评论流程
def zb_comment(member_key):

    #获取直播老师ID
    seller_id_list = loop_seller_id(num)

    #判断获取直播老师ID是否成功
    if seller_id_list != 0:
        for i in range(0, len(seller_id_list)):
            
            #获取对应老师直播间的第一条直播
            policy_id = gxs_zb_details(seller_id_list[i])

            #判断获取老师直播间第一条直播是否成功
            if policy_id != 0:
                #增加等待时间
                wait_time(time_config['comment_maxtime'])
                gxs_zb_comment(member_key, policy_id)
                
    else:
        print "直播评论流程中止!!!".decode('utf-8')

#答疑解惑流程
def zb_dyjh(member_key):

    #获取疑难解惑老师ID
    seller_id_list = loop_seller_id(yljh_num)

    #判断获取疑难解惑老师ID是否成功
    if seller_id_list != 0:
        for i in range(0, len(seller_id_list)):
            answer_question(member_key, seller_id_list[i])
    else:
        print "获取老师ID失败!!!".decode('utf-8')
            
    

