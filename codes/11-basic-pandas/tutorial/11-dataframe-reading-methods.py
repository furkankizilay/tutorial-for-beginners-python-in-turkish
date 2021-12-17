import pandas as pd
import openpyxl

#CSV Dosyası Okuma
dataset = pd.read_csv("USvideos.csv")
print(dataset)

newdataset = dataset.drop(["video_id", "trending_date"], axis= 1)
print(newdataset)

#CSV Dosyası Yazma
#newdataset.to_csv("UsVideosNew.csv")
#Yeni bir dosya oluşturuldu

#newdataset.to_csv("UsVideosNew.csv",index=False) #İndex değerleri yazdırılmıcak

#------------------------------------------
print()
print()

#EXEL Okuma
excelset = pd.read_excel("excelfile.xlsx")
print(excelset)

#Değer ekleme
excelset["Column5"] = [170,180,190,200]
print(excelset)

#Farklı bir exel dosyasına kaydetme
excelset.to_excel("excelfilenew.xlsx")

#------------------------------------------------
print()
print()

new = pd.read_html("https://www.contextures.com/xlsampledata01.html", header=0)
print(new)
