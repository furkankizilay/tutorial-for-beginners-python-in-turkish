"""class Hayvan():
    def __init__(self,ad):
        self.ad=ad


class Inek(Hayvan):
    def Konus(self):
        return "möö"


class Kedi(Hayvan):
    def Konus(self):
        return "miyav"


class Köpek(Hayvan):
    def Konus(self):
        return"hav hav"

a=[Inek("inek"),
   Kedi("kedi"),
   Köpek("köpek")]

for i in a:
    print(i.ad+":"+i.Konus())"""

class Calisanlar():

    def __init__(self, isim, soyisim, maas, departman):
        self.isim       = isim
        self.soyisim    = soyisim
        self.maas       = maas
        self.departman  = departman

    def bilgileri_goster(self):
        print("İsim:", self.isim,"\n","Soyisim:", self.soyisim,"\n","Maaş:", self.maas,"\n", "Departman:", self.departman)

    def mesai_hesapla(self, mesai_saati):
        saat_ucreti  = self.maas/30/8
        mesai_ucreti = mesai_saati * (saat_ucreti * 1.2)
        print("{} çalışanına ait mesai ücreti {} Türk Lirasıdır.".format(self.isim, mesai_ucreti))

calisan_1 = Calisanlar("Mert", "Kaya", 6500, "Bilgi İşlem")

class Yonetici(Calisanlar):

    def __init__(self, isim, soyisim, maas, departman, sicil_puani):
        super().__init__(isim, soyisim, maas, departman,)
        self.__sicil_puani = sicil_puani

    def bilgileri_goster(self):
        print("İsim:", self.isim,"\n","Soyisim:", self.soyisim,"\n","Maaş:", self.maas,"\n", "Departman:", self.departman,"\n","Sicil Puanı:",self.__sicil_puani)

    def mesai_hesapla(self, mesai_saati):
        saat_ucreti  = self.maas/30/8
        mesai_ucreti = mesai_saati * (saat_ucreti * 1.4)
        print("{} yöneticisine ait mesai ücreti {} Türk Lirasıdır.".format(self.isim, mesai_ucreti))

yonetici_1 = Yonetici("Hakan", "Elmas", 9500, "Bilgi İşlem",100)

calisan_1.mesai_hesapla(5)

yonetici_1.mesai_hesapla(5)



