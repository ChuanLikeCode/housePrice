#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests as req
import re
import json
from pymongo import MongoClient

def anaylise(resultList,collection):
    try:
        info = {};
        for i in range(11):
            list = resultList[i].split("</span>")
            info[list[0]] = list[1]
        list = resultList[12].split(">")
        danjia = list[1].split('万')
        info['历史成交记录']=danjia[0]
        list = resultList[13].split('单价')
        danjia = list[1].split('元/平,')
        info['单价'] = danjia[0]
        info['成交时间'] = danjia[1]
        print('插入一条数据',end='')
        print(info)
        collection.insert_one(info)
    except IndexError as e:
        print(e)
        pass

def linkToWeb(fp,collection):
    httpLink = '-1'
    while httpLink != '':
        httpLink = fp.readline()
        if httpLink =='':
            break
        httpLink = httpLink.strip('\n')
        requests = req.get(httpLink)
        pattern = re.compile("(?:房屋户型\<\/span\>[\.0-9\u4e00-\u9fa5]+)|"
                             "(?:所在楼层\<\/span\>[\.0-9\u4e00-\u9fa5]+)|"
                             "(?:建筑面积\<\/span\>[\.0-9\u4e00-\u9fa5]+)|"
                             "(?:户型结构\<\/span\>[\.0-9\u4e00-\u9fa5]+)|"
                             "(?:建筑类型\<\/span\>[\.0-9\u4e00-\u9fa5]+)|"
                             "(?:房屋朝向\<\/span\>[\.0-9\u4e00-\u9fa5]+)|"
                             "(?:建成年代\<\/span\>[\.0-9\u4e00-\u9fa5]+)|"
                             "(?:装修情况\<\/span\>[\.0-9\u4e00-\u9fa5]+)|"
                             "(?:建筑结构\<\/span\>[\.0-9\u4e00-\u9fa5]+)|"
                             "(?:梯户比例\<\/span\>[\.0-9\u4e00-\u9fa5]+)|"
                             "(?:产权年限\<\/span\>[\.0-9\u4e00-\u9fa5]+)|"
                             "(?:配备电梯\<\/span\>[\.0-9\u4e00-\u9fa5]+)|"
                             "(?:data-signsource=\"0\"\>[\.0-9\u4e00-\u9fa5]+)|"
                             "(?:class=\"record_detail\"\>[\.0-9\u4e00-\u9fa5]+[/][\u4e00-\u9fa5][,][0-9\-]+)")
        resultList = pattern.findall(requests.text)
        anaylise(resultList,collection)

def readHouseFile():
    client = MongoClient('localhost',27017) #连接数据库
    db = client.house  # 连接数据库名称
    fileList = ['北京']
    for i in range(len(fileList)):
        fp = open(fileList[i]+'.txt','r')
        collection = db[fileList[i]] #使用collection集合，没有则自动创建
        linkToWeb(fp,collection)
        fp.close()
        print('结束'+fileList[i]+'房屋信息的获取')



if __name__ == '__main__':
    readHouseFile()



