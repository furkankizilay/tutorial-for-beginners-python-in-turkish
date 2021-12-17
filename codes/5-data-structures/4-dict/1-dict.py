for i in dir (dict):
    if"_"not in i:
        print(i,end=",")

#---------------------------------
print()
a=dict(bir=1, iki=2, uc=3) #DICT OLUŞTURMA METOTLARI
b={'bir':1, 'iki':2, 'uc':3}
c=dict(zip(['bir', 'iki', 'uc'], [1,2,3]))
d=dict([('iki',2),('bir',1),('uc',3)])
e=dict({'uc':3, 'bir':1, 'iki':2})
a==b==c==d==e
#---------------------------------
print()
S={1:"bir",2:"iki",3:"üç"}
#S=dict(bir=1, iki=2, üç=3)
print(S.setdefault(4,("dört"))) # eğer key değeri sözlükte yoksa varsayılan değeri (o da yoksa none) geri döndürür.

x=iter(S)
print(next(x))
print(next(x)) # sözlükteki anahtar değer üzernde bir iteratör gibi gezinmeyi sağlar.

print(S.get(3,("yoktur")))
print(S.get(4,("yoktur"))) #dört değeri setdefault ile sözlüğe eklendi.
print(S.get(5,("yoktur"))) # get metotu eğer key değeri sözlükte varsa değerini yoksa mesajı geri döndürür.
print(S)

print(S.pop(4)) #anahtar değeri girilen elemanı siler.
print(S)

print(S.popitem()) #sözlükten rastgele bir eleman siler.

K=S.copy()
print(K)

print(S.clear()) #sözlükteki tüm elemanları siler.

D={1:"bir",2:"iki"}
L={1:"one",2:"two"}
D.update(L)
print(D) #print'le birleşik yazılmıyor.

print(D.items()) #sözlük çiflerinin (key:value) listesini verir.(tuple olarak veriyor)
print(D.keys()) #sözlükteki key değerlerini verir.
print(D.values()) #sözlükteki value değerilerini verir.
print(len(D)) #sözlüktek eleman sayısını verir.
print(D[1]) #anahtarı belirtilen değerin karşılığını ekran çıktısı olarak verir.
del D[1]
print(D)
print(1 in D)
print(1 not in D)
