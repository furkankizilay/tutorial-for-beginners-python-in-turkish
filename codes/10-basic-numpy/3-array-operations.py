import numpy as np
from numpy.core.fromnumeric import size

print(np.array([1,2,3,4,5,6])) # Listeyi diziye dönüştürür.

print(np.arange(5)) # 0-n arası sayılardan olşan dizi oluşturur.

print(np.arange(1,10))

print(np.arange(4,20,2)) # ikişer artan dizi oluşur.

print(np.linspace(0,5,3)) # 3 adet eşit aralıklı sayılardan oluşan dizi oluşturur.

print(np.zeros(2)) # np.zeros((2,2)) matrix oluşturur.

print(np.ones(2))

print(np.repeat(9,10)) # 10 tane 9 içeren dizi oluşturur.

print(np.eye(5)) # 5 elemanlı birim matris oluşturur.

# print(np.trace(matris)) matris'in köşegenlerinin toplamını verir.

print(np.random.randn(5)) # 0-1 arasında 5 sayılık dizi oluşturur.

print(np.random.randn(2,3)) # 2 satır ve 3 sütünluk rastgele sayılardan bir matris oluşturur.

print(np.random.randint(1,100,10)) # 1 dahil 100'e kadar rastgele 10 sayılık bir array oluşturur.

print(np.random.randint(1,9,[2,5])) # 1-9 arasındaki sayılardan 2 satır 5 sütunluk bir matris oluşturur.

print(np.random.randint(20,size = 10)) # 0-20 arasında 10 elemanlı bir array oluşturdu.

print(np.random.randint(10,size = (3,5))) # 0-10 arasında 3e 5lik bir matrix oluşturur.

print(np.random.normal(10,4,[3,4])) # ortalamsı 10 standart sapması 4  olan matrix tanımlandı