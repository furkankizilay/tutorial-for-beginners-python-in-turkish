a=int(input("Kaçıncı Aydasınız:"))

if(a<=2):
    print("KIŞ")
elif(a==12):
    print("KIŞ")
elif(3<=a<=6):
    print("İLKBAHAR")
elif(6<=a<=9):
    print("YAZ")
else:
    print("Hatalı Bilgi Girdiniz")

#---------------------------------
print()
for i in range(2,20,2):
    print(i)
    if(i==10):
        break

#----------------------------------
print()
a=0
while a<=10:
    a=a+1
    if(a==2 or a==3):
        continue
    print(a)
print("Döngüden Çıkıldı")


#----------------------------------
print()
print("Dört sayı giriniz")

s1=int(input("Birinci sayı:"))
s2=int(input("İkinci sayı:"))
s3=int(input("Üçüncü sayı:"))
s4=int(input("Dördüncü sayı:"))

a=s1

if(s2<a):
    a=s2
if(s3<a):
    a=s3
if(s4<a):
    a=s4

print("Sonuç",a)

#-------------------------------
print()
a=int(input("Notunuzu Girin:"))

if(a>=90):
    print("AA")
elif(80<=a<=89):
    print("BA")
elif(70<=a<=79):
    print("BB")
elif(60<=a<=69):
    print("CB")
elif(50<=a<=59):
    print("CC")
elif(a<50):
    print("FF")
else:
    print("Hatalı Bilgi Girdiniz")

#----------------------------
print()
a=int(input("Birinci Sayı:"))
b=int(input("İkinci Sayı:"))
c=input("İşlem:")

if(c=="+"):
    x=a+b
elif(c=="-"):
    x=a-b
elif(c=="*"):
    x=a*b
elif(c=="/"):
    x=a/b
else:
    print("Hatalı Giriş Yaptınız")

print("Sonuç:",x)
