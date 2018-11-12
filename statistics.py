#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from pymongo import MongoClient
from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import json
from bson.objectid import ObjectId
# collection = db['成都']
# rs = collection.find()
# df = DataFrame(list(rs))
# df = df.astype({'历史成交记录': 'float'})
# reslist = df['历史成交记录'].describe()
# reslist = df['历史成交记录'].value_counts()
# print(reslist)

# collection = db['成都']
# rs = collection.find()
# df = DataFrame(list(rs))
# 将某一列转换类型
# df = df.astype({'成交时间':'float'})
# reslist = df['成交时间'].mean()
# print(reslist)

# 计算每一列的值出现的重复次数
# reslist = df['成交时间'].value_counts()
# result = DataFrame(reslist)
# dict_country = result.to_dict( 'dict')
# print(reslist)
# print(dict_country['成交时间'])
# insertCollection = db['成都Count']
# insertCollection.insert_one(dict_country['建筑结构'])

# 统计各个城市的属性数量
# typeList = ['房屋户型','所在楼层','户型结构','建筑类型','房屋朝向','建成年代',
#                 '装修情况','建筑结构','梯户比例','产权年限','成交时间']
#  建筑面积 历史成交记录 单价
# count
# mean
# std
# min
# 25%
# 50%
# 75%
# max
def inputFileJsonBeijin():
    client = MongoClient('localhost', 27017)  # 连接数据库
    db = client.house  # 连接数据库名称
    file = open('json/北京.json', 'w')
    collection = db['北京Count']
    result = list(collection.find())
    for j in range(len(result)):
        del result[j]['_id']
    json.dump(result, file, ensure_ascii=False)
    file.close()
    print('完成北京的统计----JSON转换')

def beij():
    client = MongoClient('localhost', 27017)  # 连接数据库
    db = client.house  # 连接数据库名称
    collection = db['北京']
    insertCollection = db['北京Count']
    typeList = ['房屋户型','所在楼层','户型结构','建筑类型','房屋朝向','建成年代',
                '装修情况','建筑结构','梯户比例','产权年限','成交时间']
    describeList = ['建筑面积','历史成交记录','单价']
    rs = collection.find()
    df = DataFrame(list(rs))
    del df['配备电梯']
    df = df.astype({'建筑面积': 'float','历史成交记录': 'float','单价': 'float'})
    for j in range(len(typeList)):
        reslist = df[typeList[j]].value_counts()
        result = DataFrame(reslist)
        dict_country = result.to_dict('dict')
        insertCollection.insert_one(dict_country[typeList[j]])
        print(dict_country)
    for k in range(len(describeList)):
        reslist = df[describeList[k]].describe()
        result = DataFrame(reslist)
        dict_country = result.to_dict('dict')
        insertCollection.insert_one(dict_country[describeList[k]])
        print(dict_country)
    print('完成统计')


    #  去除不干净的数据 历史成交记录
    # over = 1
    # while over == 1:
    #     over = 0
    #     try:
    #         rs = collection.find()
    #         df = DataFrame(list(rs))
    #         del df['配备电梯']
    #         df = df.astype({ '历史成交记录': 'float'})
    #     except ValueError as e:
    #         over = 1
    #         error = str(e)
    #         reslut = error.replace('\'', '')
    #         reslut = reslut.split(' ')
    #         print(reslut[6])
    #         removeList = df[df['历史成交记录'].isin([reslut[6]])].to_dict('list')
    #         removeList = removeList['_id']
    #         print(removeList)
    #         for i in range(len(removeList)):
    #             collection.delete_one({"_id": removeList[i]})
    #             print('移除一条数据')

def count():
    client = MongoClient('localhost', 27017)  # 连接数据库
    db = client.house  # 连接数据库名称
    fileList = ['上海','东莞','中山','佛山','南京','厦门',
                '合肥','大连','天津','广州','廊坊','惠州',
                '成都','杭州','武汉','沈阳','济南','海口',
                '深圳','烟台','石家庄','苏州','西安','重庆','长沙','青岛']
    # fileList = ['北京']
    typeList = ['房屋户型','所在楼层','户型结构','建筑类型','房屋朝向','建成年代',
                '装修情况','建筑结构','梯户比例','产权年限','成交时间']
    describeList = ['建筑面积','历史成交记录','单价']
    for i in range(len(fileList)):
        collection = db[fileList[i]]
        insertCollection = db[fileList[i] + 'Count']
        rs = collection.find()
        df = DataFrame(list(rs))
        df = df.astype({'建筑面积': 'float','历史成交记录': 'float','单价': 'float'})
        for j in range(len(typeList)):
            reslist = df[typeList[j]].value_counts()
            result = DataFrame(reslist)
            dict_country = result.to_dict('dict')
            insertCollection.insert_one(dict_country[typeList[j]])
            print(dict_country)
        for k in range(len(describeList)):
            reslist = df[describeList[k]].describe()
            result = DataFrame(reslist)
            dict_country = result.to_dict('dict')
            insertCollection.insert_one(dict_country[describeList[k]])
            print(dict_country)
        print('完成'+fileList[i]+'的统计')

# 将文件转成json形式保存来画图
def inputFileJson():
    client = MongoClient('localhost', 27017)  # 连接数据库
    db = client.house  # 连接数据库名称
    fileList = ['北京','上海', '东莞', '中山', '佛山', '南京', '厦门',
                '合肥', '大连', '天津', '广州', '廊坊', '惠州',
                '成都', '杭州', '武汉', '沈阳', '济南', '海口',
                '深圳', '烟台', '石家庄', '苏州', '西安', '重庆', '长沙', '青岛']
    nameList = ['beijin','shanghai','dongguan','zhongshan','foshan','nanjin','xiamen','hefei','dalian','tianjin','guangzhou','langfang','huizhou',
                'chengdu','hangzhou','wuhan','shengyang','jinan','haikou','shengzhen','yantai','shijiazhuang','suzhou','xian','chongqin',
                'changsha','qingdao']
    for i in range(len(fileList)):
        file = open('js/' + fileList[i] + '.js', 'w')
        collection = db[fileList[i] + 'Count']
        result = list(collection.find())
        for j in range(len(result)):
            del result[j]['_id']
        file.write('var '+nameList[i] + '= ' + str(result))
        # json.dump('var shanghai = '+str(result), file, ensure_ascii=False)
        file.close()
        print('完成' + fileList[i] + '的统计----JS转换')

# 计算每个城市的成交价格、单价、面积 随时间的走势
def computed():
    client = MongoClient('localhost', 27017)  # 连接数据库
    db = client.house  # 连接数据库名称
    fileList = ['北京', '上海', '东莞', '中山', '佛山', '南京', '厦门',
                '合肥', '大连', '天津', '广州', '廊坊', '惠州',
                '成都', '杭州', '武汉', '沈阳', '济南', '海口',
                '深圳', '烟台', '石家庄', '苏州', '西安', '重庆', '长沙', '青岛']
    nameList = ['beijin', 'shanghai', 'dongguan', 'zhongshan', 'foshan', 'nanjin', 'xiamen', 'hefei', 'dalian',
                'tianjin', 'guangzhou', 'langfang', 'huizhou',
                'chengdu', 'hangzhou', 'wuhan', 'shengyang', 'jinan', 'haikou', 'shengzhen', 'yantai', 'shijiazhuang',
                'suzhou', 'xian', 'chongqin',
                'changsha', 'qingdao']
    for i in range(len(fileList)):
        collection = db[fileList[i]]
        rs = collection.find()
        df = DataFrame(list(rs)).astype({'建筑面积': 'float','历史成交记录': 'float','单价': 'float'})
        reslist = df.groupby(['成交时间']).mean().reset_index().to_dict('list')
        file = open('jscount/'+fileList[i]+'count.js', 'w')
        file.write('var ' + nameList[i] + 'count = ' + str(reslist) + '\n export { '+ nameList[i] + 'count }')
        file.close()
        print('完成----' + fileList[i] + '-----的统计----JS---Count转换')

# 计算房屋朝向
def computedsss():
    client = MongoClient('localhost', 27017)  # 连接数据库
    db = client.house  # 连接数据库名称
    fileList = ['House','北京']
    nameList = ['house','beijin']
    for i in range(len(fileList)):
        collection = db[fileList[i]]
        rs = collection.find()
        df = DataFrame(list(rs))
        # df = DataFrame(list(rs)).astype({'建筑面积': 'float', '历史成交记录': 'float', '单价': 'float'})
        reslist = df.groupby(['成交时间','房屋朝向'])
        res_list = {}
        for name, group in reslist:
            if res_list.__contains__(name[0]):
                res_list[name[0]]['date'] = name[0]
                res_list[name[0]][name[1]] = group.shape[0]
            else:
                res_list[name[0]] = {'东': 0,'南': 0,'西': 0,'北': 0,'东南': 0,'东北': 0,'西南': 0,'西北': 0,'暂无数据': 0}
                res_list[name[0]]['date'] = name[0]
                res_list[name[0]][name[1]] = group.shape[0]
        data_list = []
        for name in reslist:
            data_list.append(res_list[name[0][0]])
        file = open('housediretion/' + fileList[i] + 'direction.js', 'w')
        file.write('var ' + nameList[i] + 'direction = ' + str(data_list) + '\n export { ' + nameList[i] + 'direction }')
        file.close()
        print('完成----' + fileList[i] + '-----的统计----JS---Count转换')
        # print(data_list)

def translation_direction():
    client = MongoClient('localhost', 27017)  # 连接数据库
    db = client.house  # 连接数据库名称
    fileList = ['House', '北京']
    nameList = ['house', 'beijin']
    for i in range(len(fileList)):
        collection = db[fileList[i]]
        rs = collection.find()
        df = DataFrame(list(rs))
        # df = DataFrame(list(rs)).astype({'建筑面积': 'float', '历史成交记录': 'float', '单价': 'float'})
        reslist = df.groupby(['成交时间', '房屋朝向'])
        res_list = {}
        for name, group in reslist:
            if res_list.__contains__(name[0]):
                res_list[name[0]]['date'] = name[0]
                res_list[name[0]][name[1]] = group.shape[0]
            else:
                res_list[name[0]] = {'东': 0, '南': 0, '西': 0, '北': 0, '东南': 0, '东北': 0, '西南': 0, '西北': 0, '暂无数据': 0}
                res_list[name[0]]['date'] = name[0]
                res_list[name[0]][name[1]] = group.shape[0]
        data_list = {'date':[],'东': [], '南': [], '西': [], '北': [], '东南': [], '东北': [], '西南': [], '西北': [], '暂无数据': []}
        res_list_keys = list(res_list.keys())
        # print(res_list_keys[0])
        for j in range(len(res_list_keys)):
            data_list['date'].append(res_list[res_list_keys[j]]['date'])
            data_list['东'].append(res_list[res_list_keys[j]]['东'])
            data_list['南'].append(res_list[res_list_keys[j]]['南'])
            data_list['西'].append(res_list[res_list_keys[j]]['西'])
            data_list['北'].append(res_list[res_list_keys[j]]['北'])
            data_list['东南'].append(res_list[res_list_keys[j]]['东南'])
            data_list['东北'].append(res_list[res_list_keys[j]]['东北'])
            data_list['西南'].append(res_list[res_list_keys[j]]['西南'])
            data_list['西北'].append(res_list[res_list_keys[j]]['西北'])
            data_list['暂无数据'].append(res_list[res_list_keys[j]]['暂无数据'])
        file = open('housediretion/' + fileList[i] + 'direction.js', 'w')
        file.write('var  ' + nameList[i] + 'direction = ' + str(data_list) + '\n export { ' + nameList[i] + 'direction }')
        file.close()
        print('完成----' + fileList[i] + '-----的统计----JS---Count转换')



if __name__ == '__main__':
    translation_direction()
    # computedsss()
    # computed()
    # inputFileJsonBeijin()
    # beij()
    # count()
    # inputFileJson()