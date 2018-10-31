#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import requests as req
import json
import re
def download(url,start,end):
    for i in range(end):
        getListInfo(url,str(i+1))
# print(requests.text)
# <a  class="" href="https://hf.ke.com/ershoufang/" >二手房
# (\ < a href=\")(https:\/\/bj\.lianjia\.com\/chengjiao/[0-9]+\.html)
# h += 1
# getListInfo(httpLink + "/chengjiao/pg" + str(i + 1) + "/", h, file)
def getListInfo():
    fp = open('hoseLink.txt', 'r')
    httpLink = "-1"
    h = 0
    k = 0
    while httpLink != '':
        httpLink = fp.readline()
        if httpLink == '':
            break
        httpLink = httpLink.strip('\n')
        requests = req.get(httpLink + "/chengjiao/pg1/")
        patternname = re.compile("city_name: '[\u4E00-\u9FA5]+")
        nameList = patternname.findall(requests.text)
        name = nameList[0].replace("city_name: '", "")
        file = open(str(name)+".txt",'a+')
        k += 1
        for i in range(100):
            h+=1
            requests = req.get(httpLink + "/chengjiao/pg" + str(i + 1) + "/")
            pattern = re.compile("(\<a href=\")("+httpLink+"\/chengjiao\/[a-zA-Z0-9]+\.html)")
            resultList = pattern.findall(requests.text)
            resultList = list(map(lambda x:x[1],resultList))
            for i in range(len(resultList)):
                file.write(str(resultList[i]) + '\n')
            print("完成数据收集第" + str(h) + "条")
        print("-------------------完成数据收集第" + str(k) + "条")
        h=0
        file.close()
    fp.close()


def analysis(url,file):
    print(1111)

def initFile():
    fp = open("usefullyHouse.txt", "r")
    file = open('hoseLink.txt', 'a+')
    # httpLink = fp.readline()
    # httpLink = httpLink.strip('\n')
    # file.write(str(httpLink) + '\n')
    httpLink = "-1"
    while httpLink != '':
        httpLink = fp.readline()
        httpLink = httpLink.strip('\n')
        # analysis(httpLink, file)
        requests = req.get(httpLink+'/ershoufang/')
        pattern = re.compile("chengjiao")
        resultList = pattern.findall(requests.text)
        # print(resultList)
        if len(resultList) > 0:
            file.write(str(httpLink) + '\n')
            print(httpLink + "----收录")
        else:
            print(httpLink + "----这条没用")
    fp.close()
    file.close()

def analysisCity():
    # file = open('usefullyHouse.txt', 'a+')
    # city_name: '[\u4e00-\u9fa5]+
    requests = req.get("https://hf.ke.com")
    # pattern = re.compile("\<a  class=\"\" href=\"" + httpLink + "\/ershoufang\/\" \>二手房")

if __name__ == '__main__':
    getListInfo()
    print("完成数据收集")









