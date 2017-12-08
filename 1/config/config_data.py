#coding:utf-8

#用户数据存放
user_password = [
    {
        "teacher_mobile":"18681378808",
        "teacher_pw":"469858846"
    },

    {
        "teacher_mobile":"15921757467",
        "teacher_pw":"111111"
    },
    {
        "teacher_mobile":"15884284793",
        "teacher_pw":"123456"
    },
    {
        "teacher_mobile":"13541295760",
        "teacher_pw":"123456"
    }]



#筛选个股排序方式
stock_sort = {
    "pageNo":"2",
    "pageSize":"20",
    #sortField可配置:
    #CRAT涨幅，CVAL涨跌，HPRI最高价，LPRI最低价，NPRI最新价
    "sortField":"CRAT"
    }


#股问问题列表
question = {
    "front" : [
            "老师您好!", "请问老师，", "老师辛苦了~"
        ],
    "end" : [
            "接下来大盘走势如何，谢谢" ,"当前可以持续跟进不？" ,"适合加仓么？"
        ]


    }

#直播评论内容
comment = [
    "老师好!", "持续关注老师直播!", "谢谢老师分享~"
    ]


#直播评论次数
num = 3

#疑难解惑次数
yljh_num = 1


#疑难解惑,向老师提问问题列表
teacher_question = [
    "老师对最近大盘走势如何看待?", "老师，目前大盘风向如何?", "老师，近期股票如何控制仓位?","老师您好，目前来说，哪个版块机会较大呢？"
    ]


#流程中等待时间配置
time_config = {
    #所有流程，默认最少等待时间
    'mintime':3,
    #股机A最大等待时间
    'gja_maxtime':10,
    #股问最大等待时间
    'stockask_maxtime':15,
    #单条评论最大等待时间
    'comment_maxtime':10,
    #疑难解析最大等待时间
    'ynjx_maxtime':15
    }
