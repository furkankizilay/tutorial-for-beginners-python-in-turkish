f=open("deneme.txt","w") #w deneme.txt isimli bir dosya açtı
f.write("mesaj yazildi \n")
f.close()
#-----------------------------
f=open("deneme.txt","r") #deneme.txt okuma amaçlı açıldı
print("Dosya Adı :",f.name)
print("Kapalı mı Açık mı :",f.closed)
print("Açılış amacı :",f.mode)
f.close()
print("Kapalı mı Açık mı :",f.closed)
#----------------------------------
metin="""\nKorkma, sönmez bu şafaklarda yüzen al sancak;
Sönmeden yurdumun üstünde tüten en son ocak.
O benim milletimin yıldızıdır, parlayacak;
O benimdir, o benim milletimindir ancak."""
#dosya yazma amaçlı açıldı # denem.txt'nin önceki text'i üzerine yazılır
f=open("deneme.txt","w",encoding="utf-8")
f.write(metin)
f.close()
#-----------------------------------
#var olan dosya "a" modunda açıldı
f=open("deneme.txt","a",encoding="utf-8")
#dosyaya yeni veriler yazıldı
f.write("""\n\nÇatma, kurban olayım, çehreni ey nazlı hilal!
Kahraman ırkıma bir gül! Ne bu şiddet, bu celal?
Sana olmaz dökülen kanlarımız sonra helal...
Hakkıdır, hakk'a tapan, milletimin istiklal!""")
f.write("\nMehmet Akif Ersoy")
f.close()

#şimdi dosya açılıp, okunur
f=open("deneme.txt","r",encoding="utf-8")
print(f.readlines()) #ekran çıktısı liste halinde oldu
f.close()

#şimdi dosya açılıp, okunur
f=open("deneme.txt","r",encoding="utf-8")
while True:
    sat=f.readline() #okunanı sat'da tut
    #eğer satır sonu ise döngüden çık
    if len(sat)==0:
        break
    print(sat,) #sat içerğini ekrana yaz
f.close()
#-----------------------------------------
#var olan dosya "a" modunda açıldı
f=open("deneme.txt","a",encoding="utf-8")
#dosyaya yeni veriler yazıldı
f.write("""\n\nÇatma, kurban olayım, çehreni ey nazlı hilal!
Kahraman ırkıma bir gül! Ne bu şiddet, bu celal?
Sana olmaz dökülen kanlarımız sonra helal...
Hakkıdır, hakk'a tapan, milletimin istiklal!""")
f.write("\nMehmet Akif Ersoy")
f.close()
#şimdi dosya açılıp, okunur
f=open("deneme.txt","r",encoding="utf-8")
for lineText in f:
    print(lineText,end="")
f.close()
#---------------------------------------------
notlar=["Ömer Can :90", "Burak Can :95",
        "Levent Çoban :85","Bade Zehra :50",
        "Ekrem Yaya :65"]
#yazma amaçlı dosya açılır
f1=open("notlar.txt","w",encoding="utf-8")
for n in notlar:
    f1.write(n+"\n") #notlar alt alta yazıldı
f1.close()

#şimdi dosya açılıp okunur
print("\nAd-Soyad :Notu")
print("###########")
f2=open("notlar.txt","r",encoding="utf-8")
for n1 in f2:
    print(n1,end="")
f2.close()
#-------------------------
#notlar.txt dosyası okuma amaçlı açıldı
f=open("notlar.txt","r",encoding="utf-8")
print("Dosya Adı :",f.name)
print("Okunan Satır :",f.readline())
pos=f.tell()
print("işaretcinin pozisyonu",pos)
print("diğer satırlar",f.read())
print("işaretcinin pozisyonu",f.tell())
f.seek(0) #dosya başına konumlan
print("işaretcinin son pozisyonu",f.tell())
f.close()
#--------------------------------
with open("deneme2.txt","r") as fileObject:
    text=fileObject.read()
    print(f"Dosya adı :{fileObject.name}")
    print(text)
with open("deneme2_ters.txt","w") as fileObject:
    print(f"Dosya adı :{fileObject.name}")
    text=text[::-1]
    text=fileObject.write(text)
    print(text)
#---------------------------------
fileName=input("Metin dosyasının ismini giriniz: ")

linesNumber=0
wordsNumber=0
wordMaxLength=0

if len(fileName)>0: #dosya isminin uzunluğu 0dan büyükse aç
    with open(fileName,encoding="utf-8") as fileObject:
        for lineContent in fileObject:
            linesNumber +=1 #satır sayısını 1 arttırdık
            words= lineContent.split() #kelime sayısını bulmak için listeyi boşluklarla böldük
            wordsNumber+=len(words) #her satırdaki words sayısını topladık
            for word in words:
                if len(word)>wordMaxLength:
                    wordMaxLength=len(word)
print(f"Satır sayısı: {linesNumber} ")
print(f"Kelime sayısı: {wordsNumber}")
print(f"En uzun kelimenin uzunluğu: {wordMaxLength}")

#--------------------------------
file=open("bilgiler.txt","r",encoding="utf-8")
içerik=file.read()
print("Dosyanın içerği:")
print(içerik)
file.close()



file=open("bilgiler.txt","r",encoding="utf-8")
print(file.readline())
file.close()
#ilk satır gelir

file=open("bilgiler.txt","r",encoding="utf-8")
liste=file.readlines() #elemanları liste halinde döndürür
print(liste)
file.close()

#----------------------------------
with open("bilgiler.txt","r+",encoding="utf-8") as file:
    file.seek(10)
    file.write("deneme")
#10.indisli karakterden sonra deneme yazıldı

with open("bilgiler.txt","a",encoding="utf-8") as file:
    file.write("Mert Eraslan\n")
#dosyanın sonuna ekledik

with open("bilgiler.txt","r+",encoding="utf-8") as file:
    içerik=file.read()
    içerik="Mehmet Keper\n"+içerik
    file.seek(0)
    file.write(içerik)
#dosyanın başına ekleme yaptık

with open("bilgiler.txt","r+",encoding="utf-8") as file:
    liste=file.readlines()
    liste.insert(3,"Ahmet Baltacı\n")
    file.seek(0)
    #file.writelines(liste)
    for i in liste:
        file.write(i)
#Dosyanın ortasında değişiklik yapmak

"""
 with open("falanca.txt", "r+") as f:
...     f.truncate(10)
Bu kodlar, falanca.txt adlı dosyanın ilk 10 baytı dışındaki bütün verileri siler. Yani dosyayı yalnızca 10 baytlık bir boyuta sahip olacak şekilde kırpar.
"""