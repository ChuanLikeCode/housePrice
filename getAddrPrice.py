#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests as req
import json
import re
requests = req.get("https://zs.ke.com/chengjiao/")
print(re)
# pattern = re.compile("(?:房屋户型\<\/span\>[0-9\u4e00-\u9fa5]+)|"
#                              "(?:所在楼层\<\/span\>[0-9\u4e00-\u9fa5]+)|"
#                              "(?:建筑面积\<\/span\>[\.0-9\u4e00-\u9fa5]+)|"
#                              "(?:户型结构\<\/span\>[0-9\u4e00-\u9fa5]+)|"
#                              "(?:建筑类型\<\/span\>[0-9\u4e00-\u9fa5]+)|"
#                              "(?:房屋朝向\<\/span\>[0-9\u4e00-\u9fa5]+)|"
#                              "(?:建成年代\<\/span\>[0-9\u4e00-\u9fa5]+)|"
#                              "(?:装修情况\<\/span\>[0-9\u4e00-\u9fa5]+)|"
#                              "(?:建筑结构\<\/span\>[0-9\u4e00-\u9fa5]+)|"
#                              "(?:梯户比例\<\/span\>[0-9\u4e00-\u9fa5]+)|"
#                              "(?:产权年限\<\/span\>[0-9\u4e00-\u9fa5]+)|"
#                              "(?:配备电梯\<\/span\>[0-9\u4e00-\u9fa5]+)|"
#                              "(?:data-signsource=\"0\"\>[0-9\u4e00-\u9fa5]+)|"
#                              "(?:class=\"record_detail\"\>[0-9\u4e00-\u9fa5]+[/][\u4e00-\u9fa5][,][0-9\-]+)")
# resultList = pattern.findall(requests.text)
# dic = ['房屋户型</span>2室2厅1厨1卫',
#        '所在楼层</span>中楼层',
#        '建筑面积</span>90',
#        '户型结构</span>平层',
#        '建筑类型</span>板楼',
#        '房屋朝向</span>南',
#        '建成年代</span>未知',
#        '装修情况</span>其他',
#        '建筑结构</span>钢混结构',
#        '梯户比例</span>一梯四户',
#        '产权年限</span>70年',
#        '配备电梯</span>暂无数据',
#        'data-signsource="0">300万',
#        'class="record_detail">单价33334元/平,2018-09-28']
#
# info = {};
# for i in range(11):
#     list = resultList[i].split("</span>")
#     info[list[0]] = list[1]
# list = resultList[12].split(">")
# danjia = list[1].split('万')
# info['历史成交记录']=danjia[0]
# list = resultList[13].split('单价')
# danjia = list[1].split('元/平,')
# info['单价'] = danjia[0]
# info['成交时间'] = danjia[1]
# print('插入一条数据',end='')
# print(info)
# # 第429条错误
# # print(len(resultList))
# print(resultList)
# print(requests.text)
