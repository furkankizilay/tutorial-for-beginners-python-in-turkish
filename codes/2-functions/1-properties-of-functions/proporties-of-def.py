#Fonksiyonları return ile Dönmek
def fonksiyon(işlem_adı):
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    def çarpma(*args):
        çarpım = 1
        for i in args:
            çarpım *= i
        return çarpım

    if işlem_adı == "toplama":
        return toplama
    else:
        return çarpma
        
deneme = fonksiyon("toplama")
deneme # toplama fonksiyonuna eşit oldu.
print(deneme(1,2,3,4,5,6,7))
deneme2 = fonksiyon("çarpma")
deneme2 # çarpma fonksiyonuna eşit oldu.
print(deneme2(1,2,3,4,5,6,7,8,9))

def kayıt_oluştur(**bilgiler):
    print("-"*30)

    for anahtar, değer in bilgiler.items():
        print("{:<10}: {}".format(anahtar, değer))

    print("-"*30)

kayıt_oluştur(ad="Fırat", soyad="Özgül", şehir="İstanbul", tel="05333213232")

#** işaretlerini kullanmamız sayesinde hem adlarını hem de değerlerini kendimiz belirlediğimiz bir kişi veritabanı oluşturma imkanı elde ediyoruz.

#Fonksiyonları Argüman Olarak Göndermek
def toplama(a,b):
    return a + b
def çıkarma(a,b):
    return a-b
def çarpma(a,b):
    return a * b
def bölme(a,b):
    return a / b

def anafonksiyon(func1,func2,func3,func4,işlem_adı): # Tanımladığımız 4 fonksiyonu da argüman olarak göndereceğiz.
    if (işlem_adı == "toplama"):
        print(func1(3,4))
    elif (işlem_adı == "çıkarma"):
        print(func2(10,3))
    elif (işlem_adı == "çarpma"):
        print(func3(10,3))
    elif (işlem_adı == "bölme"):
        print(func4(10,4))
    else:
        print("Geçersiz işlem adı...")

anafonksiyon(toplama,çıkarma,çarpma,bölme,"toplama")
anafonksiyon(toplama,çıkarma,çarpma,bölme,"bölme")

#Dekatatör fonksiyonlarının oluşturulması
import time
def zaman_hesapla(fonksiyon):
    def wrapper(sayılar):
        baslama = time.time()
        sonuç = fonksiyon(sayılar)
        bitis = time.time()
        print(fonksiyon.__name__ + " " + str(bitis - baslama) + " saniye sürdü.")
        return sonuç
    return wrapper

@zaman_hesapla
def kareleri_hesapla(sayılar):
    sonuç = []
    for i in sayılar:
        sonuç.append(i ** 2)
    return sonuç

@zaman_hesapla
def küpleri_hesapla(sayılar):
    sonuç = []
    for i in sayılar:
        sonuç.append(i ** 3)
    return sonuç
#1. kareleri_hesapla fonksiyonu zaman_hesapla fonksiyonuna argüman olarak gidiyor.
#2. wrapper fonksiyonu kareleri_hesapla fonksiyonuna argüman olarak gönderilen
#"sayılar" argümanını argüman olarak alıyor.sd
#3. wrapper fonksiyonu hem zaman hesaplama işlemini gerçekleştiriyor,hem de gönderilen
#fonksiyonu çalıştırıyor. Böylelikle bu fonksiyona ekstra özellik ekliyor.
#4.zaman_hesaplama fonksiyonu en son işlem olarak wrapper fonksiyonumuzu dönüyor.
#------------------------
def ekstra(fonk):
    def ekstra_ozellik():
        print("Mükemmel Sayılar...")
        for sayı in range(1, 1001):
            toplam = 0
            i = 1
            while (i < sayı):
                if (sayı % i == 0):
                    toplam += i
                i += 1
            if (toplam == sayı):
                print(sayı)
        fonk()
    return ekstra_ozellik

@ekstra
def asal_sayılar():
    print("Asal Sayılar...")
    for sayı in range(2, 1001):
        i = 2
        say = 0
        while (i < sayı):
            if (sayı % i == 0):
                say += 1
            i += 1
        if (say == 0):
            print(sayı)
asal_sayılar()