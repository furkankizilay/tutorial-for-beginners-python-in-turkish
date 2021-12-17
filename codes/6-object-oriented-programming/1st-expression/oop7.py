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