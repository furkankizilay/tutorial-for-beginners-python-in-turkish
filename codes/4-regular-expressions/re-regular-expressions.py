#re modülü import re şeklinde çağırılmalıdır.
#re modüülne ait metotlar dir(re) komutu ile listelenir.
import re

s="bir ol iri ol diri ol"
ara=re.match("ol",s)
print(ara)
#none çünkü string başı ile eşleşmedi
ara2=re.match("bir ol",s)
print(ara2)

#fullmatch metodu metnin tamamı ile eşleşmezse none çıktısı verir
liste=["ali","ayşe","bade","sare"]
#adı a veya b ile başlayan ve e ile bitin isimleri arıyoruz.
for isim in liste:
    if(re.search("^[ab].*e$",isim)):
        print(isim)
# ^ karakteri stringin başını ifade eder $ ifadenin başını gösterir. * kendinden önceki ifadenin tekarlanacağını belirtir.
ara4=re.split(" ",s)
print(ara4)
#metini boşluk karakterine göre parçalara ayırdı

tekerleme="kartal kalkar,dal sarkar,dal sarkar,kartal kalkar"
değiştir=re.sub("sarkar","kalkar",tekerleme)
print(değiştir)

siir="yar_olur,ağyar_olur,seradar_olur,dildar_olur"
sonOlur=re.findall("\w+olur",siir) #sonu "olur" ile biten kelimeleri al # \w alfa numerik karakterleri belirtir
print(sonOlur)

#purge ragex belleğini temizler
#escape çıkış karakterini verir

email=input("e-mail adresini gir:")
rMailkontrol=r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$"
#e mail kontrol stringi
m=re.search(rMailkontrol, email)

if m:
    print("geçerli adres:",m.group())
else:
    print("geçersiz adres, lütfen tekrar deneyiniz")