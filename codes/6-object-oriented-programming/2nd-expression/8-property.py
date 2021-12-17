"""class Çalışan():
    personel = []

    def __init__(self, isim):
        self.isim = isim
        self.personele_ekle()

    def personele_ekle(self):
        self.personel.append(self.isim)
        print('{} adlı kişi personele eklendi'.format(self.isim))

    @classmethod
    def personeli_görüntüle(cls):
        print('Personel listesi:')
        for kişi in cls.personel:
            print(kişi)

    def isim_değiştir(self, yeni_isim):
        kişi = self.personel.index(self.isim)
        self.personel[kişi] = yeni_isim
        print('yeni isim:', yeni_isim)

İsimi bir metotla değiştirik
ç1.isim_değiştir('Emre')
"""

class Çalışan():
    _personel = []

    def __init__(self, isim):
        self._isim = isim
        self.personele_ekle()

    def personele_ekle(self):
        self._personel.append(self._isim)
        print('{} adlı kişi personele eklendi'.format(self._isim))

    @classmethod
    def personeli_görüntüle(cls):
        print('Personel listesi:')
        for kişi in cls._personel:
            print(kişi)

    @property # @property bezeyicisinin yaptığı en temel iş, bir metodu, nitelik gibi kullanılabilecek hale getirmektir.
    def isim(self):
        return self._isim

    @isim.setter
    def isim(self, yeni_isim):
        kişi = self._personel.index(self.isim)
        self._personel[kişi] = yeni_isim
        print('yeni isim: ', yeni_isim)

c1 = Çalışan()
c1.isim = 'Emre'

"""
Dolayısıyla, kodlarınızı kullananların değiştirmesini istemediğiniz, ‘salt okunur’ nitelikler oluşturmak için @property bezeyicisinden yararlanabilirsiniz.
Eğer amacınız değişkeni salt okunur hale getirmek değilse @property ile bezediğimiz fonksiyon için bir setter parametresi tanımlayabilirsiniz.
.setter bezeyicisini, bir niteliği yazılabilir hale getirmenin yanı sıra, doğrulama işlemleri için de kullanabilirsiniz.
Bu arada, .setter dışında .deleter adlı özel bir @property bezeyicisi daha bulunur. Bunu da bir değeri silmek için kullanıyoruz:
"""

"""
class Program():
    def __init__(self):
        self._sayı = 0

    @property
    def sayı(self):
        return self._sayı

    @sayı.setter
    def sayı(self, yeni_değer):
        if yeni_değer % 2 == 0:
            self._sayı = yeni_değer
        else:
            print('çift değil!')

        return self.sayı

    @sayı.deleter
    def sayı(self):
        del self._sayı
        

Gördüğünüz gibi, @property bezeyicisini kullanırken üç ayrı metot tanımlıyoruz:

İlgili niteliğe nasıl ulaşacağımızı gösteren bir metot: Bu metodu @property ile beziyoruz.

İlgili niteliği nasıl ayarlayacağımızı gösteren bir metot: Bu metodu @metot_adı.setter şeklinde beziyoruz.

İlgili niteliği nasıl sileceğimizi gösteren bir metot: Bu metodu @metot_adı.deleter şeklinde beziyoruz.
"""