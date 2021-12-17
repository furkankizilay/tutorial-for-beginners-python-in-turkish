class Dosya():
    def __init__(self):
        with open("metin.txt","r",encoding="utf-8") as file:
            dosya_icerigi = file.read()
            kelimeler = dosya_icerigi.split()
            self.sade_kelimeler = list()

            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")
                self.sade_kelimeler.append(i)

    def tum_kelimeler(self):
        kelimeler_kümesi = set()

        for i in self.sade_kelimeler:
            kelimeler_kümesi.add(i)
        print("Tüm kelimeler........")

        for i in kelimeler_kümesi:
            print(i)
            print("********************************")

    def kelime_frekansı(self):
        kelime_sözlük = dict()

        for i in self.sade_kelimeler:
            if (i in kelime_sözlük):
                kelime_sözlük[i] += 1
            else:
                kelime_sözlük[i] = 1

        for kelime,sayı in kelime_sözlük.items():
            print("{} kelimesi {} defa geçiyor....".format(kelime,sayı))
            print("--------------------------------------------------")

dosya = Dosya()
dosya.kelime_frekansı()
#-----------------------------------------
bin(4) # bin fonksiyonu . Sayımız 2'lik tabanda yazıldı. (1 ve 0)
#'0b100'
bin(19) # bin fonksiyonu . Sayımız 2'lik tabanda yazıldı. (1 ve 0)
#'0b10011'
hex(32) # Sayımız 16'lık tabanda yazıldı.
#'0x20'
hex(54) # Sayımız 16'lık tabanda yazıldı.
#'0x36'
#abs fonksiyonu
#Sayının mutlak değerini almamızı sağlar.
#round fonksiyonu
#Sayıları alta veya üste yuvarlar.
#round(3.21329321321323,4) # Ondalıklı sayının 4. hanesine göre yuvarlar
#3.2133
#max ve min fonksiyonu
#max() fonksiyonu verdiğimiz değerlerin en büyüğünü döndürür.
#min() fonksiyonu verdiğimiz değerlerin en küçüğünü döndürür.
#sum fonksiyonu
#sum() fonksiyonu verilen değerleri toplayarak döndürür. Değerlerin liste,demet vb. şeklinde verilmesi gerekir.
#pow fonksiyonu
#pow() fonksiyonu üs alma işlemlerinde kullanılır.
