for i in dir (list):
    if"_"not in i:
        print(i,end=",")

L=[1,3,5,7,9]
L.append(11)  #L listesine 11 elemanını ekler sadece bir eleman ekler.
print(L)
print()
L2=[13]
L.extend(L2) #L listesine L2 listesini ekler L+=L2 de aynı işlemi yapar
print(L)
print()
L.insert(7,15) #0 dan başlanmaz normal şekilde sayılır(8)
print(L)
print()
L.remove(15) #listedeki ilk 15 elemanını siler
print(L)
print()
L.pop(6)
print(L) #listeden 6 indisli numarayı siler
print()
L.reverse()
print(L)  #L listesinin elemanalrını ters çevirir
print()
L.sort()
print(L) #L listesinin elemanlarını küçükten büyüğe sıralar
print()
L3=L.copy()
print(L3)  #L listesinin bir kopyasını oluşturur #iki liste biribine eşitleneceği zaman l3=l2.copy() yapılır yapılmazsa l2 de veya l3 de yapılan her değişiklik her seferinde ikisinide etkiler.
print()
print(L.count(11)) #L listesindeki 11 elemanının adedini verir
print()
print(L.index(11)) #11 elemanının indisini döndürür
print()
L.clear()
print(L) #L listesindeki tüm elemanları siler. delL[:] de aynı işlemi yapar.sadece listenin elemanalrını siler liste silinmez.