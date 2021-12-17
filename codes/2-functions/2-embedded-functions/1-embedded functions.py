#map Fonksiyonu :
#map(fonksiyon, iterasyon yapılabilicek(for ile üstünde gezinilebilicek) veritipi(liste,demet,...))
#ekran çıktısı vermesi için liste dönüştürülmesi lazım

def double(x):
    return x * 2
map(double,[1,2,3,4,5,6,7]) # fonksiyon bir tane argüman alıyor ve listenin her bir elemanı üzerinde uygulanıyor.
#<map at 0x5522e9e208>
list(map(double,[1,2,3,4,5,6,7]))
#[2, 4, 6, 8, 10, 12, 14]

#Buradaki fonksiyonları lambda ifadeleriyle de yazabiliriz.
map(lambda x : x ** 2, [1,2,3,4,5,6,7,8,9])
#<map at 0x5522e9e438>
list(map(lambda x : x ** 2, [1,2,3,4,5,6,7,8,9]))
#1, 4, 9, 16, 25, 36, 49, 64, 81]

#Map fonksiyonu birden fazla liste veya demet alabilir.
liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = [9,10,11,12,13]

map(lambda x,y : x * y , liste1,liste2)
#<map at 0x5522e9e2b0>
list(map(lambda x,y : x * y , liste1,liste2))
#[5, 12, 21, 32]
list(map(lambda x,y,z : x * y * z , liste1,liste2,liste3))
#[45, 120, 231, 384]

#--------------------------------------------
#reduce Fonksiyonu :

#reduce fonksiyonunu kullanmak için functools kütüphanesini import etmek gerekir
#from functools import reduce
#reduce(fonksiyon, iterasyon yapılabilicek(for ile üstünde gezinilebilicek) veritipi (liste,vb.) )
#reduce() fonksiyonu değer olarak aldığı fonksiyonu soldan başlayarak listenin ilk iki elemanına uygular ve daha sonra çıkan sonucu
#listenin 3. elemanına uygular ve bu şekilde devam ederek liste bitince bir tane değer döner.

from functools import reduce  # reduce fonksiyonu son sürümlerde functools modülüne taşındı.
reduce(lambda x,y : x + y , [12,18,20,10])
#60

reduce(lambda x,y : x * y , [1,2,3,4,5])
#120

reduce(lambda x,y : x * y , [3,4,5,10])
#600

# max fonksiyonu()
max([1,2,3,4,5,6])
#6
# reduce ile max fonksiyonu
def maksimum(x,y):
    if (x > y):
        return x
    else:
        return y

reduce(maksimum, [-2,1,100,35,32])
#100

#----------------------------------------------
#filter Fonksiyonu:

#filter(fonksiyon, iterasyon yapılabilicek(for ile üstünde gezinilebilicek) veritipi (liste,vb.) )
#ekran çıktısı vermesi için liste dönüştürülmesi lazım
#filter fonksiyonu birinci parametre olarak mutlaka mantıksal değer dönen (True/False) bir fonksiyon alır ve
#liste gibi veri tiplerinin her bir elamanına bu fonksiyonu uygular. filter sadece True sonuç çıkaran değerleri alarak bir tane filter objesi döner.

filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8,9,10])
#<filter at 0xa4bab50438>
list(filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8,9,10])) # Çift olan sayılar
#[2, 4, 6, 8, 10]
def asal_mi(x):
    i = 2
    if (x == 1):
        return False # Asal değil
    elif(x == 2):
        return True # Asal sayı
    else:
        while(i < x):
            if (x % i == 0):
                return False # Asal Değil
            i += 1
    return True
asal_mi(34)
#False
asal_mi(2)
#True
asal_mi(1)
#False
asal_mi(3)
#True
asal_mi(4)
#False

filter(asal_mi,range(1,100))
#<filter at 0xa4bab50550>
list(filter(asal_mi,range(1,100))) # 1 den 100' e kadar olan asal sayılar.

#--------------------------------------------
#zip Fonksiyonu :

liste1 = [1,2,3,4,5]
liste2 = [6, 7, 8, 9, 10, 11]

# sonucu [(1,6),(2,7),(3,8),(4,9),(5,10)] yapmaya çalışalım.

i = 0
sonuç = list()
while (i < len(liste1) and i < len(liste2)):
    sonuç.append((liste1[i], liste2[i]))

    i += 1
print(sonuç)
[(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
#Peki böyle uzun bir işlemi zip fonksiyonuyla nasıl yaparız ? İsterseniz zip fonksiyonunun kullanımını direk örnek üzerinden görelim.

zip(liste1, liste2)
#< zip at 0x2744933988 >
list(zip(liste1, liste2))
[(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
#Burada zip fonksiyonunun kullanımını görüyoruz.zip fonksiyonu listelerin elemanları sırasıyla demet şeklinde gruplayarak bir
#tane liste oluşturuyor.Başka bir örnek yapalım.

liste1 = [1, 2, 3, 4]
liste2 = [5, 6, 7, 8]
liste3 = ["Python", "Php", "Java", "Javascript", "C"]
list(zip(liste1, liste2, liste3))
#[(1, 5, 'Python'), (2, 6, 'Php'), (3, 7, 'Java'), (4, 8, 'Javascript')]

## Aynı anda iki liste üzerinde gezinmek
liste1 = [1, 2, 3, 4]
liste2 = ["Python", "Php", "Java", "Javascript"]

for i, j in zip(liste1, liste2):
    print("i:", i, "j:", j)
#i: 1 j: Python
#i: 2 j: Php
#i: 3 j: Java
#i: 4 j: Javascript

# Sözlükleri zipleyelim.
sözlük1 = {"Elma": 1, "Armut": 2, "Kiraz": 3}
sözlük2 = {"Sıfır": 0, "Bir": 1, "İki": 2}
list(zip(sözlük1, sözlük2))  # Anahtarlar eşleşti.
#[('Elma', 'Sıfır'), ('Armut', 'Bir'), ('Kiraz', 'İki')]
list(zip(sözlük1.values(), sözlük2.values()))  # Değerler eşleşti
#[(1, 0), (2, 1), (3, 2)]

#------------------------------------------
#Enumerate Fonksiyonu

liste = ["Elma", "Armut", "Muz", "Kiraz"]
# sonucu [(0,'Elma'),(1,'Armut'),(2,'Muz'),(3,'Kiraz')] yapmak istiyoruz.
sonuç = list()
i = 0
for a in liste:
    sonuç.append((i, a))
    i += 1
print(sonuç)
#[(0, 'Elma'), (1, 'Armut'), (2, 'Muz'), (3, 'Kiraz')]

#Yani aslında burada herbir elemanı indekslerle numaralandırıyor ve demet çiftleri oluşturuyoruz.
# for döngüsü yazarken bazen hem elemanları hem de indeksleri almak isteyebiliriz.
# Böyle bir durumda numaralandırma işlemi yapan enumerate fonksiyonunu kullanabiliriz.

liste = ["Elma","Armut","Muz","Kiraz"]
list(enumerate(liste))
#[(0, 'Elma'), (1, 'Armut'), (2, 'Muz'), (3, 'Kiraz')]

liste = ["a","b","c","d","e","f","g"]

for index,eleman in enumerate(liste):
    if (index % 2 == 0):
        print("Eleman: ",eleman)

#Eleman:  a
#Eleman:  c
#Eleman:  e
#Eleman:  g

#------------------------------------
#all Fonksiyonu:

#all() fonksiyonu bütün değerler True ise True, en az bir değer False ise False sonuç döndürür.
liste = [True,False,True,False,True]
all(liste)
#False
liste = [1,2,3,4,5]
all(liste)
#True

#any Fonksiyonu:

#any() fonksiyonu bütün değerler False ise False, en az bir değer True ise True sonuç döndürür.
liste = [True,False,True,False,True]
any(liste)
#True
liste = [0,0,0,0,0,0,0]
any(liste)
#False

#---------------------------------
#örnekler
def alan_hesapla(demet):
    return demet[0] * demet[1]

liste = [(3,4),(10,3),(5,6),(1,9)]
print(list(map(alan_hesapla,liste)))

#-----
from functools import reduce
liste = [1,2,3,4,5,6,7,8,9,10]

filtre = list(filter(lambda x : x % 2 == 0,liste))
print(reduce(lambda x,y : x + y,filtre))

#-----
isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

for i,j in zip(isimler,soyisimler):
    print(i,j)

#--------------------------------
from functools import reduce

def double(x):
    return x*2
print(list(map(double,[1,2,3,4,5])))
print(list(map(lambda x:x*2,[1,2,3,4,5])))

print(reduce(lambda x,y:x*y,[1,2,3,4,5,6,7,8,9]))

print(max(1,2))
def maksimum(x,y):
    if x>y:
        return x
    else:
        return y
print(reduce(maksimum,[1,120,159,378]))

print(list(filter(lambda x:x%2==0,[2,5,6,8,9,4,3,7,1])))

liste1=[1,2,3,4,5,6,7,8,9]
liste2=[9,8,7,6,5,4,3,2,1]
print(list(zip(liste1,liste2)))
for i,j in zip(liste1,liste2):
    print("i:",i,"j:",j)


liste3=["Elma","Armut"]
print(list(enumerate(liste3)))

liste4=["a","b","c","d","e"]
for index,eleman in enumerate(liste4):
    if index%2==0:
        print("Elemean",eleman)