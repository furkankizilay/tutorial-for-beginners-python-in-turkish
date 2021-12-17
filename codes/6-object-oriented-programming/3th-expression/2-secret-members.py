class Han():
    def __init__(self):
        self.zar=1
        self._zar=2
        self.__zar=3

a=Han() #a nesnesi üretildi
print(a.zar)
print(a._zar)
#print(a.__zar) hata verir.

a=Han()
print(a._Han__zar)
print(Han().__dict__)

#---------------------------------------------------------------

class urun:
    def __init__(self):
        self.__fiyat=1000
    def fiyatYaz(self):
        print("Ürün fiyatı :",self.__fiyat)
    def setFiyat(self,fiyat):
        self.__fiyat=fiyat

u=urun()
u.fiyatYaz()

u.__fiyat=900 #1000 lira değişmedi kapsülledik değişmedi
u.fiyatYaz()

u.setFiyat(500)
u.fiyatYaz()

#---------------------------------------------------------------

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

#-----------------------------------------------------------------

#class üyeleri ve erişim biçimleri
class sporcu():
    def __init__(self,ad,brans,altın,gumus,bronz):
        self.ad=ad
        self.brans=brans
        self.mbronz=bronz #public data
        self._mgumus=gumus #semi private
        self.__maltın=altın #private
    def atlet_bilgisi(self): #bilgileri geri döndericek
        return "sporcu adı: {}, branşı: {}".format(atlet1.ad,atlet1.brans)
    def a_yazdır(self): #altına ulaşmak için fonksiyon tanımladık
        a_madalya=self.__maltın
        return a_madalya
atlet1=sporcu("ateş","100 metre",2,3,5) #adına ve branşına erişebildik
#print(atlet1.ad,atlet1.bras) #def atlet_bilgisi diye bir fonksiyon tanımladığımız için bunu kullanmıyoruz.
print(atlet1.atlet_bilgisi())
print("bronz madalya sayısı",atlet1.mbronz) #bronz madalyalrının görünmesine izin veriyor.
print("gümüş madalya sayısı",atlet1._mgumus) #yazarken kısayollarda çıkmaz kendimizin yazması lazım.
#print("altın madalya sayısı",atlet1.__maltın) #data erişilemez
print("altın madalya sayısı",atlet1.a_yazdır())
