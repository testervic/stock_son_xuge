#coding:utf-8

#用户数据存放
user_password = [
    {
        "teacher_mobile":"18511903584",
        "teacher_pw":"654321"
    },
    {
        "teacher_mobile":"18382133273",
        "teacher_pw":"123456"
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
    },
    {
        "teacher_mobile":"13551833814",
        "teacher_pw":"123456"
    }]
'''
user_password = [

    {
        "teacher_mobile":"13541295760",
        "teacher_pw":"123456"
    },
    {
        "teacher_mobile":"13551833814",
        "teacher_pw":"123456"
    },
    
    {   "teacher_mobile":"18681378808",
        "teacher_pw":"123456"
    }]
'''
#筛选个股排序方式
stock_sort = {
    "pageNo":"1",
    "pageSize":"4000",
    #sortField可配置:
    #CRAT涨幅，CVAL涨跌，HPRI最高价，LPRI最低价，NPRI最新价
    "sortField":"CRAT"
    }


#股问问题列表
question = {
    "front" : [
            "老师你好!",
            "请问老师，",
            "老师辛苦了~"，
            "老师，"
        ],
    "end" : [
            "未来走势如何，谢谢？",
            "当前可以持续跟进不？",
            "适合加仓么？",
            "如何操作？",
            "有上涨空间不？",
            "怎么样？",
            "应该减仓吗？"
        ]


    }

#直播评论内容
comment = [
    "老师好!",
    "持续关注老师直播!",
    "谢谢老师分享~",
    "给老师点赞！",
    "老师的直播很精彩~",
    "老师辛苦了！",
    "期待老师的解说~"
    ]


#评论和疑难解惑控制
zb_num = {
    #直播评论次数
    "comment_num":3,
    #疑难解惑次数
    "yljh_num":1,
    #直播列表提供筛选老师数量
    "seek_num":20
}

#疑难解惑,向老师提问问题列表
teacher_question = [
    "老师对最近大盘走势如何看待?",
    "老师，目前大盘风向如何?",
    "老师，近期股票如何控制仓位?",
    "老师您好，目前来说，哪个版块机会较大呢？",
    "请问，钢铁板块还能持续跟进吗？",
    "老师看好重金属板块吗？",
    "老师对石墨烯板块怎么看？",
    "最近哪个板块表现会更值得期待呢？",
    "老师，物联网板块是否有机会？",
    "请问近期MSCI概念板块是否具有冲击力？"
    ]


#流程中等待时间配置
time_config = {
    #所有流程，默认最少等待时间
    'mintime':1,
    #股机A最大等待时间
    'gja_maxtime':3,
    #股问最大等待时间
    'stockask_maxtime':5,
    #单条评论最大等待时间
    'comment_maxtime':5,
    #疑难解析最大等待时间
    'ynjx_maxtime':5
    }

hosts_config = ''

'''
hosts_config = "# APP inner web\n\
192.168.10.205 static.guxiansheng.cn\n\
192.168.10.205 login.api.guxiansheng.cn\n\
192.168.10.205 u.api.guxiansheng.cn\n\
192.168.10.205 content.api.guxiansheng.cn\n\
192.168.10.205 trade.api.guxiansheng.cn\n\
192.168.10.205 h5api.api.guxiansheng.cn\n\
192.168.10.205 h5.api.guxiansheng.cn\n\
192.168.10.205 tpsadmin.guxiansheng.cn #第三方内网\n\
192.168.10.205 tps.api.guxiansheng.cn #第三方内网\n\
192.168.10.205 pay.api.guxiansheng.cn\n\
192.168.10.205 managertps.guxiansheng.cn\n\
192.168.10.205 merchants.guxiansheng.cn\n\
192.168.10.205 newh5.guxiansheng.cn\n\
192.168.0.96 manager.tps.cn\n\
192.168.10.205   zb.gukezhibo.com#直播\n\
192.168.10.205   gkadmin.gukezhibo.com\n\
192.168.10.205   gkcustomer.gukezhibo.com\n\
192.168.10.205   static.guxiansheng.cn\n\
192.168.10.205	wxlgd.guxiansheng.cn\n\
192.168.10.205 front.caixuetang.cn\n\
120.76.180.146 mk2.api.guxiansheng.cn\n\
192.168.10.205 www.guxiansheng.cn\n\
192.168.10.205 m.guxiansheng.cn\n\
192.168.10.243 cfzx.testtg.com\n\
192.168.10.205 clb.api.guxiansheng.cn\n\
192.168.10.205 seller.api.guxiansheng.cn\n\
192.168.10.205 hegui.guxiansheng.cn #合规后台\n\
192.168.10.205 compliance.api.guxiansheng.cn\n\
192.168.10.205 www.guxiansheng.cn\n\
120.76.180.146 mk.api.guxiansheng.cn\n\
192.168.10.205 admin.caixuetang.cn\n\
192.168.10.205 api.caixuetang.cn\n\
192.168.10.205 zhifu.caixuetang.cn\n\
192.168.10.205 front.caixuetang.cn\n\
192.168.10.205 doc.caixuetang.cn\n\
192.168.10.205 edu.caixuetang.cn"
'''
