class Çalışan():
    personel = []

    def __init__(self, isim):
        self.isim = isim
        self.kabiliyetleri = []
        self.personele_ekle()

    @classmethod
    def personel_sayısını_goruntule(cls):
        print(len(cls.personel))

    def personele_ekle(self):
        self.personel.append(self.isim)
        print('{} adlı kişi personele eklendi'.format(self.isim))

    def personeli_görüntüle(self):
        print('Personel listesi:')
        for kişi in self.personel:
            print(kişi)

    def kabiliyet_ekle(self, kabiliyet):
        self.kabiliyetleri.append(kabiliyet)

    def kabiliyetleri_görüntüle(self):
        print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
        for kabiliyet in self.kabiliyetleri:
            print(kabiliyet)

ç1 = Çalışan("Ahmet")
ç2 = Çalışan("Mehmet")

ç1.isim = "Mahmut"

Çalışan.personel_sayısını_goruntule()
ç1.personeli_görüntüle()

ç1.kabiliyet_ekle('prezantabl')
ç1.kabiliyet_ekle('konuşkan')

ç1.kabiliyetleri_görüntüle()

ç2.kabiliyet_ekle('girişken')

ç2.kabiliyetleri_görüntüle()