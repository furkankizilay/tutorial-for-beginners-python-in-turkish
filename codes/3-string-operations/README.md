# Karakterler Diziler ve String İşlemleri

"String" kelimesi bazı kaynaklarda Türkçeye **"katar,dizge dize"** gibi sözcüklerle tercüme edilir. String değişkenler; Unicode karakterlerin (harflerin,sayıların, ve +,-,&, gibi diğer özel simgelerin) saklandığı sözel/metinsel değişkenlerdir. C dilindeki karşılığı ile bir string aynı zamanda bir karakter dizgisidir. Python dilinde değişkenleri str veri tipi ile ifade edilirler. Python dili çift tırnak "" tek tırnak '' veya üç tırnak '''...''' içerisinde yazılan her şeyi string olarak algılar.

## String Biçimlendirme Operatörleri ( % )
String içersinde sayısal veya sözel bir değişken içeriğini yazdırmak için % operatörü kullanılabilir. 

Tam sayı değişkenlerini ifade etmek için **%d**, string değişkenlerini ifade etmek için **%s**, kesirli ifadeleri ifade etmek için **%f** (sadece virgülden sonraki 2 basamağı ifade etmek için %2.f) kullanılır. String ifadeden sonra yazdırlıcak değişken isimlerinin önüne **%** operatörü konmalıdır.

## Tek Bir Stringin (Karakter Dizgisin) Elemanların Erişim
String işlemlerde ve sıralı/ardışık listelerde değişken ismini takiben parantez içersinde belirtilen numaraya **indis** adı verilir. Bir strigin her bir elamanına ayrı dizilerde/listelerde olduğu gibi indis numarası ile erişebiliriz.

## Stringlerin Dilimelme ve Birleştirme
Stringler üzerinde toplama, çarpma işlemleri gerçekleştirebiliriz. İki string ifadeyi birleştimek için + ifadesi kullanılır.

## String Dilimleme Operatörü ( : )
Stringleri parçalara ayırmak için **':'** operatörü kllanılır. String dilimeleme işleminde ':' operatörü kullanım şekli.



    strDizi [ilkİndis: sonİndis: adımMiktarı] 


Eğer ilk indis değeri belirtilmezse '0', son indis belirtilmezse 'dizinin toplam uzunluğu' kabul edilir. Adım miktarının varsayılan miktarı '1' dir. 

S[1::2] 1. indisli elemandan başla ve ikişer atlayarak dizi sonuna git. S[1:6:3] 1. indisli elemandan başla ve 6.indisli elemana kadar 3'er 3'er git.

## Bir Stringi Silmek :
Python, bir stringin elemanlarının doğrudan silinmesine izin vermez. Fakat bir stringi bir bütün olarak silebilirsiniz. Bunun için **del** gibi fonksiyonları kullanabilirsiniz. Bir stringi silemiyoruz ama stringi listeye dönüştürüp, pop fonksiyonu ile indis numarası vererek silebilirsiniz.

## Python String/Sayısal Dönüşümleri :
Python'da string/sayısal dönüşümlerde; dönüştürülecek ifade o veri tipi sarmalına alınır. Örneğin, integer veri tipini string veri tipine dönüştürürken ifade 'int' sarmalına alınırken; tersi durumunda 'str' sarmalına alınır.
