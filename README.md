# housePrice
爬取贝壳网的二手房成交数据
![交易的成交价格和建筑面积](https://github.com/ChuanLikeCode/housePrice/blob/master/%E5%8E%86%E5%8F%B2%E6%88%90%E4%BA%A4%E6%95%B0%E6%8D%AE%E5%92%8C%E5%BB%BA%E7%AD%91%E9%9D%A2%E7%A7%AF.png?raw=true)
![北京](https://github.com/ChuanLikeCode/housePrice/blob/master/%E5%8C%97%E4%BA%AC.png?raw=true)
- 包含两个爬虫
  1. 爬取单个房屋的链接
  2. 爬取房屋的主要信息
# 爬取单个房屋链接
## 爬虫文件
## getHouse.py
- 由于贝壳网上的城市很多，有的城市二手房页面没有成交记录，所以首先必须筛选出有成交记录的城市，由于本人新手，是根据正则匹配**[二手房]**
  1. 爬取有成交记录的城市首页
  2. 爬取出每个城市的成交记录


