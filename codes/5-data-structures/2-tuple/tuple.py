for i in dir (tuple):
    if"_"not in i:
        print(i,end=",")
#--------------------------------
import sys
import timeit

evenNumberList=[]
for i in range(1,101):
    if(i%2==0):
        evenNumberList.append(i)

evenNumberTuple=tuple(evenNumberList)

print(evenNumberTuple)

print("List size:",sys.getsizeof(evenNumberList))
print("Tuple size:",sys.getsizeof(evenNumberTuple)) #tuple list'den daha az yer kaplar
print("List time test:",timeit.timeit(stmt="numbers=[1,2,3,4]"))
print("Tuple time test:",timeit.timeit(stmt="numbers=(1,2,3,4)"))

#-------------------------------------
print()
string="Python"

stringList=list(string)
stringTuple=tuple(string)

print(stringList)
print(stringTuple)

string2="Python is awsome"

stringTuple=tuple(string2.split())
print(stringTuple) #tuple'lar del ile silinir ama tuple'da index atayıp belli bir değeri silemeyiz.

tuple=("Bir")
tuple1=("Bir",)
tuple2=("Bir","İki")
print(type(tuple))
print(type(tuple1))
print(type(tuple2))

#for döngüsü ve if'le item oluşturmayı tuple'larda kullanmayız.
#çünkü tuple'da append metotdu bulunmaz.


t=(1,2,3,4)

#t[1]=5 #hata mesajı verir tuple'larda index numarası vererek bir elemanı değiştiremeyiz.

x,y,z,q=t

x=11

print(t) # x'i hala 1 olarak basıcak 11 değerinini kabul etmiyecek.

t=(x,y,z,q)
print(t) #yeni bir tuple oluşturduğumuz için artık x değeri 11 olarak basılıcak.

v=([1,2,3],[4,5,6])
print(v)
v[0][2]=30
print(v) #burada tuple değişmedi tuple'ın içindeki list'de değişiklik yaptık.

