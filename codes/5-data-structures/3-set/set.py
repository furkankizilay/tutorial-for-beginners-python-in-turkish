for i in dir (set):
    if"_"not in i:
        print(i,end=",")
#------------------------------
k={"elma","armut","mandalina"}
k={1,2,3,4,5}
a=set('abracadabra')
b=set('alacazam')
k=set()
#--------------------------------
primeNumbers={2,3,5,7,11,13}
primeNumbers.add(17)
print(primeNumbers)
primeNumbers.add(6)
primeNumbers.add(True)   #add 1 item ekler
primeNumbers.add("Furkan") #add list küme tuple eklemez.
print(primeNumbers)
primeNumbers.remove(True)
print(primeNumbers)
#kümede olmayan bir elemanı silemeye çalışırsak hata alırız.
#.discard olmayan bir elemanı sildiğinde hata almaz, normal elemanları da siler.
primeNumbers.pop()
print(primeNumbers)
#Python'a göre kümenin son elemanı bilinmedği için herhangi bir elemanı siler.eğer hiç eleman yoksa pop hata verir.
primeNumbers.update({23,29},[31,37])
print(primeNumbers)
primeNumbers.clear()  #clear kümenin elemanarını siler kümeyi silmez.
print(primeNumbers)
del(primeNumbers)
#print(primeNumbers)
#update ile listeler tuple'lar setler dictler ekleyebiliriz.
#insert mototdü kümelerde çalışmaz.

evenNumber={number for number in range(2,51,2)}
print(evenNumber)

oddNumbers={number for number in range (1,51,2)}
print(oddNumbers)

multiplesOfThree={number for number in range(3,51,3)}
print(multiplesOfThree)

multiplesOfFive={number for number in range(5,51,5)}
print(multiplesOfFive)

#kümelerde sıralama yoktur o yüzden sırası değiştiriliyor.
#eleman sayılarını len fonksiyonu ile öğreniriz.

print(len(evenNumber))
print(len(oddNumbers))
print(len(multiplesOfThree))
print(len(multiplesOfFive))

sampleSet=set()
print(len(sampleSet))

print(evenNumber | oddNumbers) # | birleşim sembolüdür.
print(evenNumber.union(oddNumbers))

print(evenNumber & multiplesOfFive) #kesişim sembolüdür.
print(evenNumber.intersection(multiplesOfFive))

print(evenNumber - multiplesOfFive) #- fark sembolüdür.
print(evenNumber.difference(multiplesOfFive))

print(evenNumber ^ multiplesOfThree) #^ simetrik fark sembolüdür.
print(evenNumber.symmetric_difference(multiplesOfFive))


sampleSet1={3,5,7,9}

if sampleSet1 <= oddNumbers:  # alt kümesini olup olmadığını sorguluyoruz.
    print("sampleSet is subset of oddNumbers")

#<= yerine .issubset de kullanılabilirdi.
#öz alt kümesi olup olmadığını anlamak için = çıkarılır.

if oddNumbers >= sampleSet1:  # kapsayıp kapsamadığına bakmak için kullanılır.
    print("sampleSet is subset of oddNumbers")

#>= yerine .issuperset de kullanılabilirdi.
#bir kümenin diğer bir kümeye denk olup olmadığını == ile sorgulatırız.

#--------------------------------
print()
string="Python is awesome"
stringSet=set(string) #stringimizi kümeye dönüştürdük.
print(stringSet)
stringSet=set(string.split()) #split cümleyi kelimelere parçalayıp liste oluşturdu, set ise oluşan listeyi kümeye çevirdi.
print(stringSet)


vowels={"a","e","i","o","u"}
string2="Python is awesome"
stringSet2=set(string2)
stirngVolwes=stringSet2 & vowels
print(stirngVolwes)
print(len(stirngVolwes))

# kümelerde sıralama olmadığı için index nuamrası verip bir elemanına ulaşamayız.

#--------------------------------
print()
string=input("This is an example for Ptyhon")

words=set(string.split()) #split stringi listeye dönüştürdü set ise listeyi kümeye dönüştürdü.

print(f"This sentence is consist of {len(words)} words.")

