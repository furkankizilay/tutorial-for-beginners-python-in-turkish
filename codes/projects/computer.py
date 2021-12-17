class bilgisayar() :
    zam = 1.20
    def __init__(self,marka,fiyat):
        self.marka = marka
        self.fiyat = fiyat

    def fiyatYaz(self):
        print("Ürün fiyatı :",self.__fiyat)
    def setFiyat(self,fiyat):
        self.__fiyat=fiyat
    def etiket(self):
        return "Marka : {} Fiyat : {}".format(self.marka,self.__fiyat)
    def kurEtkisi(self):
        self.__fiyat = self.__fiyat * self.zam
    def __str__(self):
        return "Marka : {}\nFiyat : {}".format(self.marka,self.fiyat)

class monitor(bilgisayar) :
    def __init__(self,marka,fiyat,inch,hz):
        super().__init__(marka,fiyat)
        self.inch = inch
        self.hz = hz
        self.zam = 1.10
    def bilgileri_goster(self):
        return "Marka : {} Fiyat : {} Inch : {} Hz : {}".format(self.marka,self.fiyat,self.inch,self.hz)
    def __str__(self):
        return "Marka : {}\nFiyat : {}\nInch : {}\nHz : {}".format(self.marka,self.fiyat,self.inch,self.hz)


class işlemci(bilgisayar) :
    def __init__(self,marka,fiyat,nesil,bellek):
        super().__init__(marka,fiyat,nesil,bellek)
        self.nesil = nesil
        self.bellek = bellek
    def __str__(self):
        return "Marka : {}\nFiyat : {}\nNesil {}\nBellek : {}".format(self.marka,self.fiyat,self.nesil,self.bellek)

comp1 = bilgisayar("Acer",8000)
comp2 = bilgisayar("Monster",9000)

monitor1 = monitor("Samsung",1500,24.3,120)
print(monitor1.bilgileri_goster())



"""comp1.fiyat = 8500
comp2.fiyat = 9500

comp1.fiyatYaz()
comp2.fiyatYaz()

comp1.setFiyat(8500)
comp2.setFiyat(9500)

comp1.fiyatYaz()
comp2.fiyatYaz()

print(comp1.etiket())
print(comp2.etiket())

comp1.kurEtkisi()
comp2.kurEtkisi()

comp1.fiyatYaz()
comp2.fiyatYaz()"""