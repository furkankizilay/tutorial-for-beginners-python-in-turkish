import numpy as np

# numy çerisinde tek tip veri tutar
# np.array([3.14,5,7,9],dtype = "int")
# np.full([3,5],10)

liste1 = [1,2,3,4,5]

arr = np.array(liste1)
print(liste1)
print(arr) # aradaki fark arr yapısında virgül konmuyor araya
print(np.sqrt(arr)) # değerlerin karekökünü alır
print(arr[1]) # 1.indeksli değeri döndürür
print(arr[1:5]) #1. indeksli değerden 5. indeksli elemana kadar değer döndürür
print(arr[::2])
#arr2 = arr
#print(arr2[0]) #1 arr'nin 1'i
#print(arr[0]) #1 arr'nin 1'i
#arr2[0]=12 #bu şekilde değeri değiştirdiğimizde arr de değişti
#print(arr) #ilk eleman 12
#print(arr2) # ilk eleman 12
#arr2 = arr.copy()
#arr2[0] = 12
#print(arr) # arr'nin birinci elemanı hala 1
#print(arr2) # sadece arr2'nin 1. elemanı değer değiştirdi
print("---------------")

liste2 = [[1,2,3],[4,5,6],[7,8,9]]

arr2 = np.array(liste2)
print(arr2) #ekran çıktısı üç'e üçlük bir matris gibi olur.
print(arr2[2][2]) #arr2'nin 2. listesinin 2. elemanının değerini döndürür
print(arr2[2,2])
print(np.linalg.det(arr2)) #matrisin determinantını bulur
print(arr2.reshape(3,3))

print("----------------")

arr3 = np.array([10,20,30])

print(arr3) #array'in içinde de liste oluşturulabilir.
print("-----------------")

print(np.arange(1,5)) #1 den 5'e kadar olan sayıların arrayini verir
print("-----------------")

print(np.zeros(10)) # ekran çıktısı 10 adet 0 olur
print(np.ones((3,6))) #ekran çıktısı 3'e 6lık birlerden oluşan bir matrisdir.
print("-----------------")

print(np.linspace(0,100,5)) #0 dan 100'e kadar olan değerleri 5 eşit parçaya böler
print("------------------")

print(np.eye(6)) #6ya 6lık birim matris oluşturur.
print("------------------")

print(np.random.randint(5,10,2)) # 5 ile 10 arasında 2 farklı int değeri döndrür
print(np.random.rand(5)) # 0-1 arasında 5 değer döndürür
print(np.random.randn(2)) #-1 - 1 arasında 2 değer döndürür.
print("---------------------")

arr4 = np.random.randint(1,100,10)
print(arr4.max())
print(arr4.min())
print(arr4.sum())
print(arr4.mean()) #değerlerin ortlaması
print(arr4.argmax()) #en büyükdeğerin indeksi
print(arr4.argmin()) #en küçük değerin indeksi
print("---------------------")

print(arr+10) # arr'nin değerlerine teker teker 10 ekledi
arr6 = np.array([10,20,30,40])
arr7 = np.array([1,2,3,4])
print(arr6+arr7)
print("----------------------")

newArray = np.arange(1,21)
newArray=newArray.reshape(5,4)
print(newArray)
print(newArray[:2]) # ekran çıktısı olarak ilk iki satır verilir
print(newArray[:,:2]) # ekran çıktısı olarak tüm satırlar ve ilk iki sütün verilir

# np.concatenate([a1,a2,a3]) # 3 arrayi birleştirir.
# np.concatenate([a4,a5]) # a4 ve a5 matrixlerini axis default olarak 0 olduğı için satır bazaında birleştirdi
# np.concatenate([a4,a5], axis = 1) # stun bazında birleştirdi.

arr10 = np.array([1,2,3,4,5,6,7,8,9])
g1,g2,g3 = np.split(arr10,[3,5]) # arr10 arrayini 3'e kadar ve 5'e kadar böl. 3 farklı array oluşturur.

g4 = np.arange(16).reshape(4,4)
ust,alt = np.vsplit(g4,[2])
print(ust)

sol,sag = np.hsplit(g4,[2])
print(sag)