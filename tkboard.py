"""
# file owner: Kenny
# Chiu update bg color
==== 1. =====
請參考 73-tkinter-label-2文字擺放place.py

使用tkinter 建立
一個視窗
上面顯示label
產品的資料

"""

import tkinter as tk # 在Python 3.x 匯入該tkinter 函式庫
win = tk.Tk()        # 步驟2：建立GUI 應用程式的主視窗
win.wm_title("123") # 步驟3：設定主視窗標題
win.resizable(width=True, height=True) # 步驟4：設定主視窗不可以被調整大小
win.minsize(width=240, height=240)      #  最小尺寸
win.maxsize(width=1024, height=768)      #  最大尺寸
win.configure(bg='#fbbc93')
label1 =tk.Label(win,text="產品的資料")  # 建立文字
label1.place(x=50, y=50)                 # 指定元件位置 x=20, y=60 的位置

label1 =tk.Label(win,text="產品的資料")  # 建立文字
label1.place(x=50, y=50)                 # 指定元件位置 x=20, y=60 的位置

win.mainloop()       # 最後步驟：程式做無限循環

"""
==== 2. ======
使用 class 建立
一個class
儲存
產品的相關資料
"""

class partsClass(object):

    factory_area="Taoyuan"                          #定義廠區
    vendor_name="Intel"                             #定義供應商名稱
    parts_lavel="Moisture Sensitivity Level"        #定義產品管控等級
    part_category="CPU"                             #定義產品類別
    parts_number="TA987654321"                      #定義廠內料號
    parts_totle=683                                 #定義庫存數量
    unit_price=999                                  #定義單價
    parts_location="B1-FE-287"                      #定義庫位
    warehouse_temperature=23                        #倉庫溫度

    def __init__(self,area,vendor,level,category,number,total,price,location,temperature):      #初始化並定義資料
        self.factory_area = area
        self.vendor_name = vendor
        self.parts_level = level
        self.parts_category = category
        self.parts_number = number
        self.parts_total = total
        self.unit_price = price
        self.parts_location = location
        self.warehouse_temperature = temperature


    def partsInfo(self):                                    #設計函數
        print("所屬廠區:",self.factory_area)
        print("供應廠商:",self.vendor_name)
        print("管控等級:",self.parts_level)
        print("零件類別:",self.parts_category)
        print("零件編號:",self.parts_number)
        print("庫存數量:",self.parts_total)
        print("進貨單價:",self.unit_price)
        print("存放庫位:",self.parts_location)
        print("倉庫溫度:",self.warehouse_temperature)

    def callInfo(self):                                     #設計函數呼叫別的函數
        self.partsInfo()


partsClass1=partsClass(area="Taoyuan",vendor="Intel",level="Moisture Sensitivity Level",category="CPU",number="TA987654321",
                       total=683,price=666,location="B1-FE-287",temperature=23)         #啟動class


"""
==== 3. ======
請參考
65-class-properties.py

把第一題的Label 上的文字
改成讀取 class properties

"""
import tkinter as tk # 在Python 3.x 匯入該tkinter 函式庫
win = tk.Tk()        # 步驟2：建立GUI 應用程式的主視窗
win.wm_title("123") # 步驟3：設定主視窗標題
win.resizable(width=True, height=True) # 步驟4：設定主視窗不可以被調整大小
win.minsize(width=240, height=240)      #  最小尺寸
win.maxsize(width=1024, height=768)      #  最大尺寸
win.configure(bg='light blue')

label1 =tk.Label(win,text="所屬廠區:"+partsClass1.factory_area)                          # 導入資料
label1.place(x=20, y=20)                                                         # 指定位置

label1 =tk.Label(win,text="供應廠商:"+partsClass1.vendor_name)                           # 導入資料
label1.place(x=20, y=40)                                                         # 指定位置

label1 =tk.Label(win,text="管控等級:"+partsClass1.parts_level)                           # 導入資料
label1.place(x=20, y=60)                                                         # 指定位置

label1 =tk.Label(win,text="零件類別:"+partsClass1.parts_category)                         # 導入資料
label1.place(x=20, y=80)                                                         # 指定位置

label1 =tk.Label(win,text="零件編號:"+partsClass1.parts_number)                          # 導入資料
label1.place(x=20, y=100)                                                         # 指定位置

label1 =tk.Label(win,text="庫存數量:"+str(partsClass1.parts_total)+" pcs")                         # 導入資料
label1.place(x=20, y=120)                                                        # 指定位置

label1 =tk.Label(win,text="進貨單價:"+"US$ "+str(partsClass1.unit_price))             # 導入資料
label1.place(x=20, y=140)                                                        # 指定位置

label1 =tk.Label(win,text="存放庫位:"+partsClass1.parts_location)                       # 導入資料
label1.place(x=20, y=160)                                                        # 指定位置

label1 =tk.Label(win,text="倉庫溫度:"+str(partsClass1.warehouse_temperature)+" 度")     # 導入資料
label1.place(x=20, y=180)                                                        # 指定位置


win.mainloop()       # 最後步驟：程式做無限循環
