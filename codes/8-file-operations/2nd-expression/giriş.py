f = open("ilkDosya.txt","w",encoding="utf-8")
f.write("Furkan Kızılay\n")
f.write("Bahadır Kızılay\n")
metin = "Celal Batuhan Küç\nAhmet Berke İlhan\n"
f.write(metin)
f.close()

#------------------------------------------------------------
f = open("ilkDosya.txt","r",encoding="utf-8")
print("Dosya ismi :",f.name)
print("Dosyanın açıklık durumu :",f.closed)
if (f.mode == "r") :
    print("Dosyanının açılış amacı hem okuma hemde üzerine yazmaktır.")
f.close()
print("Dosyanın açıklık durumu :",f.closed)

print()
#------------------------------------------------------------
print()

f = open("ilkDosya.txt","r",encoding="utf-8")
#print(f.readlines()) # sonuç tek satır liste halinde
#print(f.readline())  # ilk satır okunur
#print(f.read()) # normal bir şekilde dosya okunur
print(f.read(14)) # 14 karakterlik veri okur

print()
#------------------------------------------------------------
print()

f = open("ikinciDosya.txt","w",encoding="utf-8")
şiir = """İstanbulu dinliyorum, gözlerim kapalı
Hafiften bir rüzgar esiyor
Yavaş yavaş sallanıyor
Yapraklar ağaçlarda
Uzaklarda çok uzaklarda
Sucuların hiç durmayan çıngırakları
İstanbulu dinliyorum, gözlerim kapalı"""
f.write(şiir)
f.write("\nOrhan Veli Kanık")
f.close()

f = open("ikinciDosya.txt","r",encoding="utf-8")
#print(f.readline()) # ilk satır okunur
#print(f.read()) # normal bir şekilde okunur
for i in f :
    print(i,end="")
f.close()

print()
#------------------------------------------------------------
print()

okulNumaraları = ["Furkan : 1062","Bahadır : 2620",
                  "Batuhan : 235","Berke : 598"]
f = open("üçüncüDosya.txt","w",encoding="utf-8")
for i in okulNumaraları :
    f.write(i+"\n")
f.close()

f = open("üçüncüDosya.txt","r",encoding="utf-8")
#print(f.read())
for i in f :
    print(i,end="")
f.close()

print()
#------------------------------------------------------------
print()

#f = open("dördüncüDosya.txt","r+",encoding="utf-8")
#print(f.read())
#print(f.tell())
#f.close()

#f = open("dördüncüDosya.txt","r+")
#f.seek(6)
#f.write("\nNesrin") # 6.indisden sonra silerek yazar
#f.close()

#f = open("dördüncüDosya.txt","a",encoding="utf-8")
#f.write("Nesrin")
#f.close()

"""f = open("dördüncüDosya.txt","r+",encoding="utf-8")
icerik = f.read()
icerik = "Musa\n"+icerik
f.seek(0)
f.write(icerik)
f.close()"""

f = open("dördüncüDosya.txt","r+",encoding="utf-8")
liste = f.readlines()
liste.insert(3,"Emir\n")
f.seek(0)
for i in liste :
    f.write(i)


