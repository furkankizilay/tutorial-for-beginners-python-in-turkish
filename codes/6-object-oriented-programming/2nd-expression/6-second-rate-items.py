class Deneme():
    def __init__(self):
        self.değer = 0
    def metot(self):
        self.metot_değeri = 1

print(Deneme())

"""
bu sınıfın birinci sınıf bir nesne olabilmesi için başka bir fonksiyona veya sınıfa parametre olarak atanabilmesi gerekiyor.
sınıfımızı print() fonksiyonuna parametre olarak atayabildik.
"""

"""
Yine yukarıdaki tanıma göre birinci sınıf nesnelerin bir fonksiyondan döndürülebilmesi gerekiyor:
"""

def fonksiyon():
    return Deneme()

print(fonksiyon())

"""
Son olarak, bir nesnenin birinci sınıf olabilmesi için bir değişkene atanabilmesi gerekiyor:
"""

değişken = Deneme()