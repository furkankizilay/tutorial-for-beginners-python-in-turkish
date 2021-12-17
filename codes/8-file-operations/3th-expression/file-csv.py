#csv modülünü import et
import csv
yeniOlay=[["22/08/2018, 8:00, Bayrampaşa, info@tek.org.tr, 5897458535, İstanbul"],
          ["26/02/2017, 9:00, Kasımpaşa, info1@tek.org.tr, 5498762539, İstanbul"]]
#OnemliOlaylar.csv dosaysını ekleme amaçlı aç
with open("OnemliOlaylar.csv","a",newline="") as f:
    ekleDosya=csv.writer(f) #ekleDosya isimli writer dosyası tanımalndı
    ekleDosya.writerows(yeniOlay) #ekleDosyaya yeni olaylar yazıldı

#csv modülünü import et
import csv
#f ile temsil edilen onemliolaylar.csv dosayasını aç
with open("OnemliOlaylar.csv","r",newline="")as f:
    #dosyadaki "," ile ayrılmış her bir veriyi okuDosya değişkeninde tut
    okuDosya=csv.reader(f,delimiter=",")
    #okuDosyadaki her bir veriyi ekrana yaz
    for satir in okuDosya:
        print(",".join(satir))

#newline="" ile dosaynın hangi satır karakterine sahip olacağı belirtilir. Kullanımı zorunludur.
#delimiter="," ile reader ile okunan her bir veri "," ile ayrılmıştır.
#------------------------------
import pickle
notlar=["Ömer Can :90", "Burak Can :95",
        "Levent Çoban :85","Bade Zehra :50",
        "Ekrem Yaya :65"]
#ikili dosya yazma amaçlı açıldı ve notlar yazıldı
with open("notlar.bin","wb")as f:
    pickle.dump(notlar,f)
#şimdi dosya açılıp okunur
with open("notlar.bin","rb") as f:
    notList=pickle.load(f)
    print(notList)
#-----------------------------
import os
print(os.getcwd())
print(os.listdir())
print(os.path.isfile("C:\\Users\\ACER\\PycharmProjects\\pythonProject\\venv\\Include"))
print(os.path.isdir("C:\\Users\\ACER\\PycharmProjects\\pythonProject\\venv\\Include"))
print(os.path.splitext("C:\\Users\\ACER\\PycharmProjects\\pythonProject\\venv\\Include\Test.py"))
#---------------------------
import urllib.request
#Text içerikli bir web sayfası gir
adres="http://shallowsky.com/python/lesson5.txt"
#web adresini aç
f=urllib.request.urlopen(adres)
#okuduğunu string formatında dosya değişkeninde tut
dosya=f.read().decode()
#dosya değikeninin içerğini ekrana yaz
print(dosya)

