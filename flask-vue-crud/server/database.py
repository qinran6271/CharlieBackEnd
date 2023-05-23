import pymongo 
import json

# 获取MongoDB Atlas连接字符串
connection_string = client = "mongodb+srv://qinran6271:vlq7DZ312Zb4oGv5@charlietest.jcnj1mr.mongodb.net/?retryWrites=true&w=majority"

# 创建MongoDB客户端
client = pymongo.MongoClient(connection_string)

# 连接到数据库
db = client.hi
collection = db.hey




