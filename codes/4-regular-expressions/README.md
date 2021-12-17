# DÜZENLİ İFADELER (REGULAR EXPRESSİONS-RE  MODÜLÜ)

Bir string veya metin içerisinde ; Python regex(düzenli ifadeler) kullanarak bu ifadelere uygun sorgulamalar yapılabilir. Regex özellikle stringlerle uğraşan programcılar için büyü kolaylık sağlar. String parçalama, ayıklama, belli kriterleye uyan verileri alma (e-mail,password kontrolü), arama (anahtar kelime araması), değiştirme gibi işlermlerde regex kullanılabilir. Bü işlemler için 're' modülü içersinde tanımlı bazı özel karakterler ve metotlar kullanılmaktadır.

## re Modülü:

Python dilinde düzenli ifadeleri kullanabilmek, yönetmek için re modülü kullanılır. 

re modülünü; *import re* şeklinde program başında çağırmak gerekir. Bu metotların listesini standart metotların isimleri ayrıştırılarak **dir(re)** komutu ile elde edilir.

* **Mach :** bir metni başka bir metin içerisinde arar, bulamazsa None değer döndürür.  
        
        re.match(“ol”,s)
* **Fullmatch :** metnin tamamı ile eşleşmezse None değer döndürür. 
        
        re.fullmatch(“bir ol”,s)
* **Split** : Bir metni belirtilen kalıba göre parçalar. 
        
        re.split(“ ”,s)
* **Sub** : bir string’i başka bir stringle değiştirir. 
        
        re.sub(“sarkar”,”kalkar”,tekerleme)
* **Findfall :** 
        
        re.findall(“\w+olur”,siir)  # sonu olur ile biten kelimeleri döndürür.