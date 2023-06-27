import pandas as pd
from pymongo import MongoClient

# 讀取 Excel 資料
excel_data = pd.read_excel('Taiwan_Taipei.xlsx') #excel檔案名稱


# 將資料轉換為 JSON 格式
json_data = excel_data.to_dict(orient='records')

# 建立到 MongoDB 的連接
client = MongoClient('mongodb+srv://<username>:<password>@travel.pdv2hg5.mongodb.net/') #username,password改成自己的

# 選擇數據庫
db = client.travel

# 創建集合
collection = db.all_city

# 插入文檔
collection.insert_many(json_data)

# 關閉連接
client.close()