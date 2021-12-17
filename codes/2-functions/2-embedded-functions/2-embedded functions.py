# abs
#abs() fonksiyonunu bir sayının mutlak değerini elde etmek için kullanıyoruz.
print(abs(-20))

#round
#round() fonksiyonu bir sayıyı belli ölçütlere göre yukarı veya aşağı doğru yuvarlamamızı sağlar.
print(round(12.4))

#all
#all() fonksiyonunun görevi, bir dizi içinde bulunan bütün değerler True ise True değeri, eğer bu değerlerden herhangi biri False ise de False değeri döndürmektir.
liste = [1,2,3,4]
print(all(liste)) # 0 hariç her sayıyı true değer olarak alır

#any
#any() fonksiyonunun görevi de, bir dizi içindeki bütün değerlerden en az biri True ise True çıktısı vermektir.

liste2 = ["Furkan","Bahadır",""]
print(any(liste2))
l = ['', 0, [], (), set(), dict()]
print(any(l)) ## içi boş bool değerleri False'dir.

#ascii
#Bu fonksiyon, bir nesnenin ekrana basılabilir halini verir bize.
print(ascii("\n1"))
#Ayrıca bu fonksiyon, karakter dizileri içindeki Türkçe karakterlerin de UNICODE temsillerini döndürür.
a = "ışık"
for i in a :
    print(ascii(i))
#ASCII olmayan karakterlerle karşılaştığında bunların karakter temsilleri yerine UNICODE temsillerini (veya onaltılık sayma düzenindeki karşılıklarını) veriyor.

#repr
#ASCII olmayan karakterlerle karşılaşsa bile, bize çıktı olarak bunalrın da karakter karşılığını gösterir
print(repr("şeker"))

#bool
#Bir nesnenin bool değerini verir
print(bool(0))

#bin
#Bir sayının ikili düzendeki karşılığını verir
print(bin(12))

#chr
#Paramtre olarak verilen bir tam sayının karakter karşılığını döndürür.
print(chr(10))

#list()
#Liste tipinde bir veri oluşturmak
#Farklı veri tiplerini liste adlı veri tipine dönüştürmek

#set()

#tuple()

#frozenset()

#dict()

#complex()
#erhangi bir sayıyı karmaşık sayıya dönüştürmeniz gerekirse complex() adlı bir fonksiyondan yararlanabilirsiniz.

#float()
#sayıları veya karakter dizilerini kayan noktalı sayıya dönüştürmek için kullanıyoruz:

#callable
#bir nesnenin çağırılabilir olup olmadığını döndürür. Fonksiyonlar çağırılabilir fakat değişkenler çağırılabilir değildir.

#dir()
#dir() fonksiyonunu parametresiz olarak kullanırsak, mevcut isim alanındaki öğeleri bir liste halinde elde ederiz:

#enumerate
print(list(enumerate("furkan")))
print(*enumerate("furkan"))

#exit()
#o anda çalışan programdan çıkmanızı sağlar.

#help
help(dir)

#format

#filter
def tek(sayı) :
    return sayı % 2 == 1
print(*filter(tek,1))

#map
def karesi(n) :
    return n**2
print(list(map(karesi,1)))

#pow

#quit

#range
#Bu fonksiyonu belli bir aralıktaki sayıları listelemek için kullanıyoruz.

#reversed
#ters çevirir

#sorted
#sıralar

#sum
#toplar

#slice
k = ['ahmet', 'mehmet', 'ayşe', 'senem', 'salih']
dl = slice(0, 3)
print(dl) #['ahmet', 'mehmet', 'ayşe']

#zip
a1 = ['a', 'b', 'c']
a2 = ['d', 'e', 'f']
zip(a1, a2)
print(*zip(a1,a2))
print(list(zip(a1,a2)))





