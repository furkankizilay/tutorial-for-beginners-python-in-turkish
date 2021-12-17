L=list("bahadır")
L.sort()
print(L)
#------------------------------
print()
A=["a","c","b","d"]
A.reverse()
B=A
print(B)
print(*B) # köşeli parantezleri yazdırmaz.
#---------------------------------------
print()
L=["ocak","şubat","mart","nisan","mayıs","haziran","temmuz","ağustos","eylül","ekim","kasım","aralık"]
ay=int(input("Kaçıncı ayda olduğunuzu girin :"))
if 1>ay>12:
    print("Yanlış değer girdiniz, girdiğiniz değer 1 ve 13 arasında olmalı.")
else:
    print(ay,".ay",L[ay-1],"'dır.")

#-------------------------------------
print()
değer=[200,100,50,20,10,5,1,0.5]
para_miktarı=float(input("Para miktarını giriniz :"))
for i in range(8):
    sayı=float(para_miktarı)//değer[i]
    if sayı!=0:
        print(sayı,"adet",değer[i])
        para_miktarı=para_miktarı-sayı*değer[i]

#------------------------------
print()
squares=list(map(lambda x:x**2, range(1,11))) #lambda işi tek satırda yapmamızı sağlıyor. map ise fonksiyonu alıp bir liste üzerinde uygulamıyı sağlıyor.
print(squares)

def f(x):
    x = x + 5
    return x

l2=[2,8,9]
print(list(map(f,l2)))
#----
l2=[2,8,9]
print(list(map(lambda x:x+5,l2))) # yukarıdaki gibi f fonksiyonu tanımlamak yerine lambda ile tek sefer kullanılıcak bir değer atadık x'e.
                                  # f(x) gibi fonksiyonları tanımlamanın yan etkisi olabiliyor. (print(x) yazdığımızda 1,2,..9 çıkıcaktı)
                                  #lambda kullanarak x'i tek seferlik kullandık işlem bitince x yok olucak.
#----
l3=[x**2 for x in range(1,11)]    # bu kullanımda da x değişkeni tanımlandı ve daha sonra x değişkeni print ettirilirse 10 değerini alıcak
print(l3)                         #bu değeri almasını biz istemediğimiz için kod devamında hataya neden olabilir.
#---
l4=[(x,y) for x in [1,2,3] for y in [4,5,6] if x!=y]
print(l4)
#---
l5=[(x,y,z) for x in [1,2,3] for y,z in [(1,8),(2,6),(7,1)] if x!=y]
print(l5)
#------------------------
print() #STACK DATA STRUCTURES
L=[3,4,5,6,7] #listeler köşeli parantezlerle belirtilirler.
L.append(8)
L.append(9)
print(L)
L.pop()
print(L)
L.pop()
L.pop()
L.pop()
print(L)

#QUEUE DATA STRUCTURES
kyrk=["Furkan","Bahadır","Nesrin","Musa"]
kyrk.append("Lale")    #Lale kuruğun sonuna eklendi
kyrk.append("Ahmet")   #Ahmet kuyruğun sonuna eklendi
kyrk.pop(0)            #Furkan kuyruktan ayrıldı
kyrk.pop(0)            #Bahadır kuyruktan ayrıldı
print(kyrk)
#---
from collections import deque
kyrk2=deque(["Tuna","Leyla","Berk"])
kyrk2.append("Can")          #Can kuruğa girdi
kyrk2.append("Mecnun")       #Mecnun kuyruğa girdi
kyrk2.popleft()              #Tuna kuruktan çıktı
kyrk2.popleft()              #Leyla kuruktan çıktı
print(list(kyrk2))

#----------------------------------
print() #MATRIS
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    for item in row:
        print(item)

#-----------------------------------
print()
names=[]
while True:
    print("3 farklı isim giriniz.")
    a=str(input("Birinci isim :"))
    b=str(input("İkinci isim :"))
    c=str(input("Üçüncü isim :"))
    names2=[a,b,c]
    if(a==b or a==c or b==c):
        print("İsimlerin farklı olası gerekiyor")
    else:
        names.extend(names2) #extend listeye başka bir liste ekler.
        print(names2)
        break

#------------------------------
print()
bad_words=["amk","aq"]

sentence=input("Bir cümle giriniz :")

words=sentence.split()
string=""
for word in words:
    if word in bad_words:
        string=string+"."
    else:
        string=string+f"{word} "

print(string)