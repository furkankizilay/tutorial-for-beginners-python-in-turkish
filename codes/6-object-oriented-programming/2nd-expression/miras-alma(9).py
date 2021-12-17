"""
Miras alınan sınıfın bütün nitelik ve metotları alt sınıfa olduğu gibi devredilir.

Miras alınan sınıfın bazı nitelik ve metotları alt sınıfta yeniden tanımlanır.

Miras alınan sınıfın bazı nitelik ve metotları alt sınıfta değişikliğe uğratılır.
"""
"""
Eğer alt sınıfa eklenen herhangi bir nitelik veya metot taban sınıfta zaten varsa, alt sınıfa eklenen nitelik ve metotlar taban sınıftaki metot ve niteliklerin yerine geçecektir.
Miras alınan üst sınıfa atıfta bulunan super() fonksiyonu, miras aldığımız bir üst sınıfın nitelik ve metotları üzerinde değişiklik yaparken, mevcut özellikleri de muhafaza edebilmemizi sağlar.

class Asker(Oyuncu):
    def __init__(self, *arglar):
        super().__init__(*arglar)
        self.güç = 100
        
def hareket_et(self):
    super().hareket_et()
    print('hedefe ulaşıldı.')

taban sınıfın hareket_et() adlı metodunu alt sınıfta tanımladığımız aynı adlı fonksiyon içinde super() fonksiyonu yardımıyla genişlettik, yani taban sınıfın hareket_et() adlı fonksiyonuna yeni bir işlev ekledik
"""