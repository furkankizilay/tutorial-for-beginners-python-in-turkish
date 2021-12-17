class Araba():
    def __init__(self,hız,renk,durum):
        self.hız=hız
        self.renk=renk
        self.durum=durum

    def __str__(self):
        return "Hız : {}\nRenk : {}\nDurum : {}".format(self.hız,self.renk,self.durum)

    def calis(self):
        print("Çalışıyor.")

    def dur(self):
        print("Duruyor.")

class kamyon(Araba):
    def __init__(self,hız,renk,durum):
        Araba.__init__(self,hız,renk,durum)
class taksi(Araba):
    def __init__(self,hız,renk,durum,km):
        Araba.__init__(self,hız,renk,durum)
        self.km=km
    def __str__(self):
        return Araba.__str__(self)+"\nKm :"+str(self.km)

k=kamyon(70,"Kırmızı",False)
print(k)
k.dur()
print("--------------------")
t=taksi(90,"Sarı",True,54000)
print(t)
t.calis()
print("--------------------")

#-----------------------------------------------------------------

#Multi inheritances
class Anne():
    def __init__(self,amiras):
        self.amiras=amiras
    def __str__(self):
        return "Anneden:"+self.amiras


class Baba():
    def __init__(self,bmiras):
        self.bmiras=bmiras
    def __str__(self):
        return "Babadan:"+self.bmiras



class Evlat(Anne,Baba):
    def __init__(self,amiras,bmiras,kendiP):
        Anne.__init__(self,amiras)
        Baba.__init__(self,bmiras)
        self.kendiP=kendiP
    def __str__(self):
        return "Mal varlığım:\nAnneden :{}\nBabadan :{}\nBenim :{}".format(self.amiras,self.bmiras,self.kendiP)

def test() :
    print("----Mirasım----")
    miras=Evlat("Zeytinlik","Villa","BMW")
    print(miras)
    print("--------------------")
if __name__ == "__main__" :
    test()

#-----------------------------------------------------------------

#Multi inheritances
class futbolcu():
    kosu="kosabilir"
    depar="depar atar"
    maas="1000"
    def __init__(self,ayak="sağ"): #oluşturucu sınıf
        self.mevki="orta saha"
        self.ayak=ayak

class basketbolcu():
    turnike="turnike atabilir"
    ucluk="ucluk atabilir"
    maas="1500"
    def __init__(self): #oluşturucu sınıfı tanımaldık
        self.bolge="ileri"
    pass
class multisporcu(basketbolcu,futbolcu): #üst iki sınıfın birleşmesinden oluşacak bu sınıfın özellikleri yukarıdaki sınıflardan gelecek.# #basketbolcu daha baskın.
    def __init__(self,ayak): #mevki'sini bastıramıyoduk bu sınıfı oluşturmasak
        basketbolcu.__init__(self)
        futbolcu.__init__(self,ayak)
    pass

ateş=multisporcu("sol")
print(ateş.turnike)
print(ateş.kosu)
print(ateş.maas)
print(ateş.bolge)
print(ateş.mevki) #futbolcunun oluşturucu sınıfını alınca hata veriyordu
print(ateş.ayak)


