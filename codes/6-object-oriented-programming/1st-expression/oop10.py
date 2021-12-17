class Tv:
    #setter fonksiyonları
    def setUz(self,u):
        self.__boy=u
    def setEn(self,e):
        self.__en=e

    #getter fonksiyonu
    def getSes(self):
        return self.__boy*self.__en

#Ana program
nesne=Tv()
frkns=nesne.setUz(10.0)
gnlk=nesne.setEn(8.0)
print("Ses Ayarı :",nesne.getSes())
print("Erişim :",dir(nesne))


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

