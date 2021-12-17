s="furkan"
liste=("fu","kan")
print("furkan".capitalize())  #s'nin ilk karakterini büyük harfe dönüştürür
print("furkan".center(10,"#")) #s'yi 10 genişliğinde genişletir ve ortalar sağ ve slundaki boşlukları # ile kapatır
print("furkan".ljust(10,"#")) #s'yi 10 uzunluğunda genişletir ve sola yaslar, sağındaki boşlukları # ile doldurur
print("furkan".rjust(10,"#")) #s'yi 10 uzunluğunda genişletir ve sağa yaslar, solundaki boşlukları # ile doldurur
print("furkan".zfill(10)) #s'yi 10 uzunluğunda genişletir ve solundaki boşlukalrı "0" ile kapatır
print("furkan".count("s")) #s'nin içindeki string adedini ekrana yazdırır
print("furkan".endswith("n")) #s'nin n ile bititp bitmediğini kontrol eder. Doğruysa True bastırır ekrana
print("furkan".startswith("f")) #s'nin f ile başlayıp başalamadığını kontrol eder. Doğruysa True bastıtı ekrana
print("furkan".find("u",0,3)) #s'nin içinde u'yu 0 indisinden başlayarak 3.karaktere kadar arar. Bulursa pozizson sırasını ekrana yazdır.
print("furkan".rfind("u",0,3)) #s'nin içindeki u değerini sağdan başlayarak arar.
print("furkan".index("u")) #find() metoduyla aynı işleve sahip bulamazsa -1 yerine Value Eror hatası verir
print("furkan".rindex("u")) #s'nin içindeki u değerini sağdan başlayarak arar.
print("furkan".expandtabs(8)) #s'nin içerisinde tab kullanıldıysa bu aralığı 8 değerinde ayarlar. Varsayılan tab değeri 8'dir.
print("r".join(liste)) #liste=("fu","kan") liste elemanlarının arasına r değerini koyar ve birleştirir.
print("".join(reversed("furkan"))) #liste elemanlarını ters sırada verir.
print("furkan".lower()) #s'yi küçük harfe dönüştürür.
print("furkan".upper()) #s'yi büyük harfe dönüştürür.
print(len("furkan")) #s'nin karakter uzunluğunu verir.
print(max("furkan")) #s'nin içindeki en son karakteri verir.(İngiliz alfabesine göre)
print(min("furkan")) #s'nin içindeki en ilk karakteri verir.(İngiliz alfabesine göre)
print("furkan".replace("a","b")) #s'nin içindeki tüm a karakterlerini b'ye çevirir.
print("Python,C,Java".split(",")) #s içerisinde belirtilen ayraç karakteri veya boşluklar dikkate alınarak metin parçalanır ve listeye dönüştürülür.
print("Pythom,C,Java".strip("Pythom,")) #s'nin başındaki ve sonundaki veya veya belirtlilen karakterleri kaldırır.
print(".furkan.co".lstrip(".co")) #s'nin sol taraftaki boşlukları veya veya belirtlilen karakterleri kaldırır. Ekran çıktısı furkan.co
print(".furkan.co".rstrip(".co")) #s'nin sağ taraftaki boşlukları veya veya belirtlilen karakterleri kaldırır. Ekran çıktısı .furkan
print("furkan".swapcase()) #s'nin büyük harflerini küçük, küçük harflerini büyük yapar.
print("furkan".title()) #s'nin sadece baş harflerini büyük harf yapar.
print("-------------------------------------")
print(s.isalnum()) # s alfenumerik ise TRUE
print(s.isalpha()) # s tamamen harf ise TRUE
print(s.isdecimal()) # s tamanem ondalık sayı tabanında ise TRUE
print(s.isdigit()) # s tamamen sayı ise TRUE
print(s.isidentifier()) # s geçerli bir değişken veya belirteç ise TRUE
print(s.islower()) # s tamamen küçük harfli ise TRUE
print(s.isupper()) # s tamamen büyük harfli ise TRUE
print(s.isnumeric()) # s tamamen sayısal karakterde ise TRUE
print(s.isprintable()) # s tamamen print edilebilrise TRUE
print(s.isspace()) # s tamamen boşluktan oluşuyorsa TRUE
print(s.istitle()) # s'da sadece ilk harfler büyükse TRUE

#string biçimlendirme
ad=str(input("Adınız:"))
soyad=str(input("Soyadınız:"))
yas=int(input("Yaşınız:"))
doğum_yeri=str(input("Doğum yeriniz:"))

print("Adınız %s,Soyadınız %s, Yaşınız %d, Doğum yeriniz %s"%(ad,soyad,yas,doğum_yeri))