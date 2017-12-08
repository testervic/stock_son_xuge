#coding:utf-8
import warnings
import time
from config.config_data import *
from function.function_common import *
from function.function_gja import *
from function.function_gxs import *
from function.function_stockask import *
from function.function_zb import *

#过滤掉警告
warnings.filterwarnings('ignore')

for teacher_num in range(0,len(user_password)):
    #分界线
    get_split_line()
    #当前用户
    print '当前运行用户'.decode('utf-8'), user_password[teacher_num]['teacher_mobile']
    #分界线
    get_split_line()    
    #获取用户id和key
    member_key = get_key(user_password[teacher_num])

    if member_key == 0:
        print '当前用户账号或密码异常，退出本次流程!!!'.decode('utf-8')
    else:
        #股机A流程
        wait_time(time_config['gja_maxtime'])
        handle_GujiA(member_key)
        #股问流程
        wait_time(time_config['stockask_maxtime'])
        stock_ask(member_key)
        #直播评论流程,已增加等待时间
        zb_comment(member_key)
        #答疑解惑流程
        wait_time(time_config['ynjx_maxtime'])
        zb_dyjh(member_key)
