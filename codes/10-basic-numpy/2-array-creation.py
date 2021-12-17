import numpy as np

d = np.arange(6)
A = d.reshape(2,3) # Tek boyulu d dizisini matrise dönüştürdü.
print(A)

print(d.shape) # boyut bilgisini verir
print(d.ndim) # boyut sayısını verir # 1
print(d.size) # eleman sayısını verir
print(d.dtype) # içindeki integerın tipini verir

d = A.ravel() # Matris'i diziye dönüştürdü.
print(d)

c = A.T # Satır ve sütunların yerini değiştirir.
print(c)

d = np.array([1,2,3,4])
ort = d.mean()
print(ort)

T = d.sum()
print(T)

T = d.prod() # Dizinin tüm elemanlarını çarpar.
print(T)

d = np.array([[1,2,3],[4,5,6]])
t = d.cumsum(axis=1) # axis=1 satırlar için yığmalı toplama işlemi yapar.
print(t) # axis=1 satır axis = 0 stun demektir.

c = d.cumprod(axis=1) # axis=1 satırlar için yığmalı çarpma işlemi yapar.
print(c)

print(d.max(axis=1))
print(d.min(axis=1))
print(d.argmax(axis=1))
print(d.argmin(axis=1))

a = np.array([[3,5,9],[4,6,1],[1,8,2]])
b = np.array([[1,0,3],[4,5,7],[2,3,6]])
T = np.matmul(a,b) # iki matrisi çarpar.
print(T)

T = np.add(a,b) # iki diziyi toplar
print(T)

d = np.array([1,2,3,4])
B = np.copy(d)
print(b)

d = np.array([1,1,2,2,3,3,4,4])
print(np.unique(d))

d = np.arange(10)
print(np.where(d>5)) # index sıralrını verir

a = np.array([3,4,5,6,2])
b = np.array([3,4,0,7,6])
c= np.intersect1d(a,b) # dizilerdeki ortak elemanları verir.
print(c)

d = np.setdiff1d(a,b) # birinci dizide olup ikinci dizide olmayan elemanları verir.
print(d)

d = np.array([3,4,1,6])
print(d.ptp()) # dizideki en büyük ve en küçük değer arasındaki farkı verir.

print(np.sort(d))

f1 = np.random.normal(20,5,(3,3))
print(np.sort(f1,axis=1)) # satırlara göre sırala

d = np.searchsorted([2,4,6],4) # dizide aranan elemanın indis numarasını döndürür.
print(d)