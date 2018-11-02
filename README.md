# housePrice
爬取贝壳网的二手房成交数据
![交易的成交价格和建筑面积](https://github.com/ChuanLikeCode/housePrice/blob/master/%E5%8E%86%E5%8F%B2%E6%88%90%E4%BA%A4%E6%95%B0%E6%8D%AE%E5%92%8C%E5%BB%BA%E7%AD%91%E9%9D%A2%E7%A7%AF.png?raw=true)
![北京](https://github.com/ChuanLikeCode/housePrice/blob/master/%E5%8C%97%E4%BA%AC.png?raw=true)
- 包含两个爬虫
  1. 爬取单个房屋的链接
  2. 爬取房屋的主要信息
## 爬取单个房屋链接
### 爬虫文件
### getHouse.py
- python版本：3.7 
- mongdb  V4.0.3
- 由于贝壳网上的城市很多，有的城市二手房页面没有成交记录，所以首先必须筛选出有成交记录的城市，由于本人新手，是根据正则匹配***二手房***
	1.   爬取有成交记录的城市首页
	2.   爬取出每个城市的成交记录
- 由于网页搜索出来有显示很多数据，有几十万，几百万条，但是一个网页显示30条数据，一共有100页，所以就是只有3000条数据，但是好在可以条件搜索，根据条件可以获取到90%的数据量，获取到的是单个房屋的成交链接
- 有些房屋交易的网页上面没有历史成交价格，所以需要把这类链接除去，用的也是正则匹配***历史成交价格***
- 时间有限，爬取信息需要大量时间
### 数据分析
- 将获取到的数据按照格式存入mongodb中，mongdb是以键值对的方式存放数据的<br/>
 info = {<br/>'房屋户型':'2室1厅1厨1卫',<br/>'所在楼层':'低楼层',<br/>'建筑面积':'54.04㎡'<br/>, '户型结构': '平层',<br/>'套内面积':'暂无数据',<br/>'建筑类型':'板楼' , <br/>'房屋朝向': '南',<br/>'建成年代':'1996',<br/>'装修情况':'简装' , <br/>'建筑结构': '砖混结构',<br/>'供暖方式':'',<br/>'梯户比例':'一梯两户' ,<br/> '产权年限': '未知',<br/>'配备电梯':'无',<br/>'历史成交记录':'295万',<br/> '单价': '54590元/平',<br/>'成交时间':'2018-10-08'<br/>}<br/>以这种方式存入数据库
- 读取数据库计算每个城市历史成交记录，单价，建筑面积的平均值、方差、最大数、最小数
### 未来期待的实现
- 研究每个城市的人都喜欢买什么样子的房子，价格，建筑面积在什么范围
- 研究每个城市的房价趋势
##多图预警
- 时间有限，数据爬取量不是很大
![城市交易单价](https://github.com/ChuanLikeCode/housePrice/blob/master/%E5%9F%8E%E5%B8%82%E4%BA%A4%E6%98%93%E5%8D%95%E4%BB%B7.png?raw=true)
![上海](https://github.com/ChuanLikeCode/housePrice/blob/master/%E4%B8%8A%E6%B5%B7.png?raw=true)
![东莞](https://github.com/ChuanLikeCode/housePrice/blob/master/%E4%B8%9C%E8%8E%9E.png?raw=true)
![中山](https://github.com/ChuanLikeCode/housePrice/blob/master/%E4%B8%AD%E5%B1%B1.png?raw=true)
![佛山](https://github.com/ChuanLikeCode/housePrice/blob/master/%E4%BD%9B%E5%B1%B1.png?raw=true)
![厦门](https://github.com/ChuanLikeCode/housePrice/blob/master/%E5%8E%A6%E9%97%A8.png?raw=true)
![合肥](https://github.com/ChuanLikeCode/housePrice/blob/master/%E5%90%88%E8%82%A5.png?raw=true)
![广州](https://github.com/ChuanLikeCode/housePrice/blob/master/%E5%B9%BF%E5%B7%9E.png?raw=true)
![深圳](https://github.com/ChuanLikeCode/housePrice/blob/master/%E6%B7%B1%E5%9C%B3.png?raw=true)
![重庆](https://github.com/ChuanLikeCode/housePrice/blob/master/%E9%87%8D%E5%BA%86.png?raw=true)
