from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from mainwindow import Ui_Dialog
import sys
from datetime import datetime, timedelta
from get_town_weather_today import *
from test import *
import random
from read_mogodb import read_db


class MainWindow(QMainWindow):
    # 縣市list
    global countyName_list
    countyName_list = ['基隆市', '臺北市', '新北市']
    global town_dict
    # 行政區名&ID dictionary
    town_dict = {'基隆市':{'中正區': '1001701', '七堵區': '1001702', '暖暖區': '1001703', '仁愛區': '1001704', '中山區': '1001705', '安樂區': '1001706'}, '臺北市':{'松山區': '6300100', '信義區': '6300200', '大安區': '6300300', '中山區': '6300400', '中正區': '6300500', '大同區': '6300600', '萬華區': '6300700', '文山區': '6300800', '南港區': '6300900', '內湖區': '6301000', '士林區': '6301100'}, '新北市':{'板橋區': '6500100', '三重區': '6500200', '中和區': '6500300', '永和區': '6500400', '新莊區': '6500500', '新店區': '6500600', '樹林區': '6500700', '鶯歌區': '6500800', '三峽區': '6500900', '淡水區': '6501000', '汐止區': '6501100', '瑞芳區': '6501200', '土城區': '6501300', '蘆洲區': '6501400', '五股區': '6501500', '泰山區': '6501600', '林口區': '6501700', '深坑區': '6501800', '石碇區': '6501900', '坪林區': '6502000', '三芝區': '6502100', '石門區': 
'6502200', '八里區': '6502300', '平溪區': '6502400', '雙溪區': '6502500', '貢寮區': '6502600', '金山區': '6502700', '萬里區': '6502800'}}
    # 星期幾的中文表示字典
    global weekdays
    weekdays = {0: '星期一', 1: '星期二', 2: '星期三', 3: '星期四', 4: '星期五', 5: '星期六', 6: '星期日'}
    #weekdays = {0: 'MON.', 1: 'TUE.', 2: 'WEN.', 3: 'THU.', 4: 'FRI.', 5: 'SAT.', 6: 'SUN.'}
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # 地區選單
        global countyName_list
        self.ui.comboBox_county.addItems(['請選擇縣市'])
        self.ui.comboBox_county.addItems(countyName_list)
        self.ui.comboBox_county.currentTextChanged.connect(self.update_town_option) # 產生鄉鎮市區選單選項
        self.ui.comboBox_town.addItems(['請選擇鄉鎮市區'])
        self.ui.comboBox_town.currentTextChanged.connect(self.comboBox_town_changed)
        
        # 日期comboBox
        self.ui.comboBox_time.addItems(["日期"])
        
        # 獲取今天日期
        current_date = datetime.now().date()
        # 生成一周日期範圍並添加到 QComboBox
        global weekdays
        for i in range(7):
            date = current_date + timedelta(days=i)
            weekday = date.weekday()  # 獲取星期幾的索引
            weekday_str = weekdays[weekday]  # 獲取星期幾的中文表示
            date_str = date.strftime("%m/%d {}".format(weekday_str))
            self.ui.comboBox_time.addItems([date_str])
        self.ui.comboBox_time.currentTextChanged.connect(self.comboBox_time_changed)

        # 天氣.setContentsMargins
        self.ui.weather_today_day_title.setContentsMargins(24,15,0,0)
        self.ui.weather_today_day.setContentsMargins(20,0,0,0)
        self.ui.weather_today_night_title.setContentsMargins(20,14,0,0)
        self.ui.weather_today_night_title_2.setContentsMargins(24,14,0,0)
        self.ui.weather_today_night.setContentsMargins(20,0,0,0)
        self.ui.weather_tomorrow_day_title.setContentsMargins(20,14,0,0)
        self.ui.weather_tomorrow_day_title_2.setContentsMargins(24,14,0,0)
        self.ui.weather_tomorrow_day.setContentsMargins(20,0,0,0)

        # 地點.setContentsMargins
        self.ui.place_01_title.setContentsMargins(20,14,0,0)
        self.ui.place_01_content.setContentsMargins(25,0,0,0)
        self.ui.place_02_title.setContentsMargins(20,14,0,0)
        self.ui.place_02_content.setContentsMargins(25,0,0,0)
        self.ui.place_03_title.setContentsMargins(20,14,0,0)
        self.ui.place_03_content.setContentsMargins(25,0,0,0)

        # 送出鍵
        self.ui.pushButton_send.clicked.connect(self.clicked_get_places)
        # 重整景點鍵
        #self.ui.pushButton_refresh_places.clicked.connect(self.clicked_press_refresh_places)

        #景點連結
        self.ui.place_01_GO.clicked.connect(self.goUrl_place_01)
        self.ui.place_02_GO.clicked.connect(self.goUrl_place_02)
        self.ui.place_03_GO.clicked.connect(self.goUrl_place_03)
    
    # 縣市&地區comboBox選項連動
    def update_town_option(self, text):
        global town_dict
        if text == "基隆市":
            self.ui.comboBox_town.addItems(['請選擇鄉鎮市區'])
            self.ui.comboBox_town.clear()
            
            self.ui.comboBox_town.addItems(town_dict['基隆市'])
            
        elif text == "臺北市":
            self.ui.comboBox_town.clear()
            self.ui.comboBox_town.addItems(['請選擇鄉鎮市區'])
            self.ui.comboBox_town.addItems(town_dict['臺北市'])
            
        elif text == "新北市":
            self.ui.comboBox_town.clear()
            self.ui.comboBox_town.addItems(['請選擇鄉鎮市區'])
            self.ui.comboBox_town.addItems(town_dict['新北市'])
            
        
        
    
    # 取得行政區資訊
    def get_townInfo(self):
        try:
            global town_dict
            countyName = self.ui.comboBox_county.currentText()
            townName = self.ui.comboBox_town.currentText()
            townID = town_dict[countyName][townName]
            townInfo = [townID, countyName, townName]
            print("====================")
            print(countyName, townName)
            print("====================")
        except:
            pass
        return townInfo

    # 天氣資訊重整
    def weather_refresh(self):
        try:
            townID = self.get_townInfo()[0]
            day = self.ui.comboBox_time.currentIndex()
            self.ui.weather_today_day.setText(get_weather_today_day(townID, day))
            self.ui.weather_today_night.setText(get_weather_today_night(townID, day))
            if day == 7:
                self.ui.weather_tomorrow_day.setText("")
            else:
                self.ui.weather_tomorrow_day.setText(get_weather_tomorrow_day(townID, day))
        except:
            pass
    # 日期&天氣資訊連動
    def comboBox_time_changed(self):
        try:
            self.day = self.ui.comboBox_time.currentText()
            self.ui.weather_today_night_title.setText(self.day)
            next_index = (self.ui.comboBox_time.currentIndex() + 1) % self.ui.comboBox_time.count()
            nextday = self.ui.comboBox_time.itemText(next_index)
            self.ui.weather_tomorrow_day_title.setText(nextday)
            self.weather_refresh()
        except:
            pass
    # 地區&天氣資訊連動
    def comboBox_town_changed(self):
        try:
            if self.ui.comboBox_time.currentIndex() != 0:
                self.weather_refresh()
        except:
            pass
    # 送出鍵 顯示景點資訊
    def clicked_get_places(self):
        countyName = self.get_townInfo()[1] # 縣市名
        try:
            townName = self.get_townInfo()[2] # 鄉鎮市區名
        except:
            pass
        try:
            week = self.day[6:]
        except:
            week = "星期一"
        
        excel_list2 = read_db(townName,week)
        self.num = random.sample(range(0,len(excel_list2)),3) #隨機3筆資料

        try:
            place_01_title = excel_list2[self.num[0]]["景點名稱"]
            place_01_content = excel_list2[self.num[0]]["簡介"]
            place_01_content2 = excel_list2[self.num[0]]["交通資訊"]
            place_02_title = excel_list2[self.num[1]]["景點名稱"]
            place_02_content = excel_list2[self.num[1]]["簡介"]
            place_02_content2 = excel_list2[self.num[1]]["交通資訊"]
            place_03_title = excel_list2[self.num[2]]["景點名稱"]
            place_03_content = excel_list2[self.num[2]]["簡介"]
            place_03_content2 = excel_list2[self.num[2]]["交通資訊"]
        except:
            place_01_title = excel_list2[0]["景點名稱"]
            place_01_content = excel_list2[0]["簡介"]
            place_01_content2 = excel_list2[0]["交通資訊"]
            place_02_title = excel_list2[0]["景點名稱"]
            place_02_content = excel_list2[0]["簡介"]
            place_02_content2 = excel_list2[0]["交通資訊"]
            place_03_title = excel_list2[0]["景點名稱"]
            place_03_content = excel_list2[0]["簡介"]
            place_03_content2 = excel_list2[0]["交通資訊"]
        #景點資訊
        self.ui.place_01_title.setText(place_01_title) # 景點01標題
        self.ui.place_01_content.setText(place_01_content) # 景點01內容
        self.ui.place_01_content_2.setText(str(place_01_content2))#交通資訊
        self.ui.place_02_title.setText(place_02_title) # 景點02標題
        self.ui.place_02_content.setText( place_02_content) # 景點02內容
        self.ui.place_02_content_2.setText(str(place_02_content2))#交通資訊
        self.ui.place_03_title.setText(place_03_title) # 景點02標題
        self.ui.place_03_content.setText( place_03_content) # 景點02內容
        self.ui.place_03_content_2.setText(str(place_03_content2))#交通資訊
    
    # GO超連結按鈕
    def goUrl_place_01(self):
        townName = self.get_townInfo()[2] # 鄉鎮市區名
        place_01_url = read_db(townName)[self.num[0]]["URL"]
        url = QUrl(place_01_url)
        QDesktopServices.openUrl(url)
    def goUrl_place_02(self):
        townName = self.get_townInfo()[2] # 鄉鎮市區名
        place_01_url = read_db(townName)[self.num[1]]["URL"]
        url = QUrl(place_01_url)
        QDesktopServices.openUrl(url)
    def goUrl_place_03(self):
        townName = self.get_townInfo()[2] # 鄉鎮市區名
        place_01_url = read_db(townName)[self.num[2]]["URL"]
        url = QUrl(place_01_url)
        QDesktopServices.openUrl(url)

    
    




if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    
    sys.exit(app.exec_())