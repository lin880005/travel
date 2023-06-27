import pandas as pd


def read_excel_town(town,weeken="星期一"):
    df = pd.read_excel('Taiwan_Taipei.xlsx')  # 讀取Excel檔案
    town_data = df[df['行政區'] == town]  # 過濾符合縣市名稱的資料
    town_data_week = town_data[town_data[weeken] == 1]
    town_data_week = town_data_week[['景點名稱', '簡介','交通資訊','URL']]  # 選取景點名稱、簡介和URL欄位
    town_name = town_data_week.to_dict(orient='list')  # 將資料轉換成字典形式
    return town_name
