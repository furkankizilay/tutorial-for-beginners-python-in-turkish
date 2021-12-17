#class Personel: #(DEKORATÖRSÜZ)
#    def __init__(self,ad,soyad):
#       self.ad=ad
#       self.soyad=soyad
#    def mail(self):
#        return "{}{}@gmail.com".format(self.ad,self.soyad)
#    def Ad(self):
#        return "{}{}".format(self.ad,self.soyad)
#    def Ad(self,isim):
#        ad,soyad=isim.split(" ")
#        self.ad=ad
#        self.soyad=soyad
#kisi1=Personel("bulent","cobanoğlu")
#kisi1.ad="bayram aksu" #KİŞİ DEĞİŞMEDİ
#print("Ad :",kisi1.ad)
#print("Soyad :",kisi1.soyad)
#print("Mail :",kisi1.mail())


class Personel: # @property dekoratörü değer atama setter değer döndürme getter, değer silme deleter amaçlarıyla kullanılabilir.
    def __init__(self,ad,soyad):
        self.ad=ad
        self.soyad=soyad
    @property #fonksiyonu parametreye dönüştürdü ve veriyi aldı bir metodu özellik gibi kullanılıcak hale getirdi.
    def mail(self):
        return "{}{}@gmail.com".format(self.ad,self.soyad)
    @property
    def Ad(self):
        return "{}{}".format(self.ad,self.soyad)
    @Ad.setter #Ad'ı set edebilme için yaptık
    def Ad(self,isim):
        ad,soyad=isim.split(" ")
        self.ad=ad
        self.soyad=soyad
kisi1=Personel("bulent","cobanoğlu")
kisi1.Ad="bayram aksu" #kişinin adını değiştirmek istedik
print("Ad :",kisi1.ad)
print("Soyad :",kisi1.soyad)
print("Mail :",kisi1.mail)

#-------------------------------------------------------

#Decorators #dışardan görüntülenmemesi ama bizimde görüp ayarlayabilmemz için kullanılır get set del
class calisan:
     def __init__(self,ad,soyad):
        self.ad=ad
        self.soyad=soyad
        #self.eposta=self.ad+self.soyad+"@sirket.com"
     @property #fonksiyonu parametreye dönüştürdü ve veriyi aldı bir metodu özellik gibi kullanılıcak hale getirdi.
     def eposta(self):
         self.email = self.ad + self.soyad + "@sirket.com"
         return self.email
     @property
     def tam_ad(self):
        return "{} {}".format(self.ad,self.soyad)
     @tam_ad.setter #tam adı set edebilme için yaptık
     def tam_ad(self,gelenisim):
         ad,soyad=gelenisim.split(" ") #gelen isimi parçaladık
         self.ad=ad
         self.soyad=soyad
     @tam_ad.deleter
     def tam_ad(self):
         self.ad=None
         self.soyad=None
         print("kullanıcı bilgileri silindi")

personel1=calisan("demir","surel")

#personel1.ad="dağra" #bu şekilde ad'ı değiştirdiğimizde e_posta'daki demir dağra olarak değişmez.

print(personel1.ad)
print(personel1.eposta) #epostanın yanına ()ekledik eklemesek değişken (object) gibi gözükücekti ekledik ve fonksiyon oldu #@property eklediğimiz için ()'i kaldırdık.
print(personel1.tam_ad)

personel1.tam_ad="dağra dağ" #bu şekilde güncellemek istedik. set edemedik
print("-------------")
print(personel1.ad)
print(personel1.eposta) #epostanın yanına ()ekledik eklemesek değişken (object) gizükücekti ekledik ve fonksiyon oldu #@property eklediğimiz için ()'i kaldırdık.
print(personel1.tam_ad)

del personel1.tam_ad

#print(personel1.ad)
#print(personel1.eposta) #epostanın yanına ()ekledik eklemesek değişken (object) gibi gözükücekti ekledik ve fonksiyon oldu #@property eklediğimiz için ()'i kaldırdık.
#print(personel1.tam_ad)
print()