class Çalışan():
    __personel = []

    def __init__(self, isim):
        self.isim = isim
        self.kabiliyetleri = []
        self.__personele_ekle()

    @classmethod
    def personel_sayısını_görüntüle(cls):
        print(len(cls.__personel))

    def __personele_ekle(self):
        self.__personel.append(self.isim)
        print('{} adlı kişi personele eklendi'.format(self.isim))

    @classmethod
    def personeli_görüntüle(cls):
        print('Personel listesi:')
        for kişi in cls.__personel:
            print(kişi)

    def kabiliyet_ekle(self, kabiliyet):
        self.kabiliyetleri.append(kabiliyet)

    def kabiliyetleri_görüntüle(self):
        print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
        for kabiliyet in self.kabiliyetleri:
            print(kabiliyet)

"""
a=Han()
print(a._Han__zar) gizli üyeye u şekilde erişebildik
print(Han().__dict__)
"""