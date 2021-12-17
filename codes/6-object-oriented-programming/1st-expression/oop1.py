class calısan: #calısanların ortak özellklerini belirleyeceğim bir class oluşturdum.
    pass

personel1=calısan()
personel1.ad="demir"
personel1.soyad="surel"
personel1.maas=3000

personel2=calısan()
personel2.ad="koray"
personel2.soyad="yıldırım"
personel2.maas=3500

print(personel2)
print(personel1) #bu şekilde bastırdığımızda objectin yerini ekran çıktısı alırız.
print(personel1.ad,personel1.soyad)  #ürettiğimiz özelliklerin ekran çıktısını almak için
print(personel2.ad,personel2.maas)
print()
#bu firmanın çalışanlarının ortak özelliklerini baştan tanımlayabilirdik.

class calisan: # init yapıcı (constructors) dell yıkıcı (destructors)
    zam_oranı=1.40 #zam oranını da dışarıdan çağırabilirdik.
    per_say=0
    def __init__(self,ad,soyad,maaş): #eğer buraya eposta yazsaydım #python bir class'dan nesne tanımlandığı zaman otomatik yapılandırıcı __init__ metodunu çağırır.
        self.ad=ad
        self.soyad=soyad
        self.maaş=maaş
        self.eposta=self.ad+self.soyad+"@sirket.com"
        calisan.per_say=calisan.per_say+1
    def tam_ad(self):
        return "Adı: {} Soyadı: {}".format(self.ad,self.soyad)
    def arttır(self):
        #self.maaş=(self.maaş*calisan.zam_oranı)
        self.maaş=(self.maaş*self.zam_oranı)
        #self.maaş=(self.maaş*zam_oranı) hata mesajı verir çünkü zam_oranı dışarıda.

personel1=calisan("demir","surel",3000)#burada epostayı benim tanımlamam gerekirdi.
print(calisan.per_say)
personel2=calisan("koray","yıldırım",3500)
print(calisan.per_say)

print(calisan.tam_ad(personel1))
print()

print(personel1.tam_ad())
print(personel1.eposta)
print(personel1.ad,personel1.maaş)

print(personel2.tam_ad())
print(personel2.eposta)
print(personel2.ad,personel2.maaş)
print()

print(personel1.maaş)
personel1.arttır()
print(personel1.maaş)
print()

print(personel2.maaş)
personel2.zam_oranı=1.50
personel2.arttır()
print(personel2.maaş)


