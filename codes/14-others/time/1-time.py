from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,"") #Türkiye olarak ayarladık
print(datetime.now()) #şuanın tarihini bastırdık
şu_an=datetime.now()
print(şu_an.year)
print(şu_an.month)
print(şu_an.day)
print(şu_an.hour)
print(datetime.ctime(şu_an)) #şuanı daha anlaşılır bastırdık
print(datetime.strftime(şu_an,"%Y")) #sadece yıl
print(datetime.strftime(şu_an,"%B")) #sadece ay ismi
print(datetime.strftime(şu_an,"%D")) #sadece gün bilgisi
print(datetime.strftime(şu_an,"%X")) #sadece saat bilgisi
print(datetime.strftime(şu_an,"%A")) #sadece gün ismi
print(datetime.strftime(şu_an,"%Y %B %A"))
saniye=datetime.timestamp(şu_an) #şuanki zamanın saniye cinsinden değeri
print(saniye)
şu_an2=datetime.fromtimestamp(saniye) #saniyeyi şuana çevirdi
print(şu_an2)
şu_an3=datetime.fromtimestamp(0) #1970 1 ocak
print(şu_an3)
tarih=datetime(2019,12,1)
şu_an4=datetime.now()
print(tarih-şu_an4)

#------------------------
from datetime import date
tarih1=date.today() #bugünkü tarihi al
print("Bugünkü Tarih : ",tarih1)
yıl=int(input("Yılı Giriniz : "))
ay=int(input("Ayı Giriniz :"))
gun=int(input("Günü Giriniz :"))
tarih2=date(yıl,ay,gun) #girileneri tarih formatına dönüştür
fark=tarih1-tarih2
print("İki tarih arası :",fark.days,"gündür.")

#--------------------------
from datetime import date,timedelta
tarih1=date.today()
print("Bugünkü tarih :",tarih1)
gun=int(input("Geçmiş gün gir :"))
gecmis=timedelta(days=gun)
tarih2=tarih1-gecmis
print(tarih2.strftime("%x"))

#--------------------------
from datetime import date
bugun=date.today() #bugünkü tarih
print("Bugünkü tarih :",bugun)
dogumGunu=date(bugun.year,12,29)
print("Doğum günüm :",dogumGunu)
if dogumGunu<bugun:
    dogumGunu=dogumGunu.replace(year=bugun.year+1)
kalanGun=abs(dogumGunu-bugun)
print("Doğum günüme kalan gün :",kalanGun.days)

#----------------------------
import calendar #Takvim
yil=int(input("Takvim yılını giriniz :"))
cal=calendar.LocaleTextCalendar(0,"TURKISH")
cal.pryear(yil)

#-----------------------------
