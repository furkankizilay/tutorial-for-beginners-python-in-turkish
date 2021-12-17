a=1
n=int(input("Tavan Sayı:"))

while(a<=n):
    b=a*a
    print(b)
    a=a+1
#-----------------------------
print()
b=int(input("Bir sayı giriniz:"))

while (b<=0)or(b>=0):
    c=b*b
    print("karesi:",c)
    if(b==0):
        break

#-------------------------------
print()
print("Hesap Makinesi")
while True:

    a=int(input("Birinci Sayıyı Giriniz:"))
    b=int(input("İkinci Sayıyı Giriniz:"))
    c=input("İşlem:")

    if(c=="+"):
        d=a+b
    elif(c=="-"):
        d=a-b
    elif(c=="*"):
        d=a*b
    elif(c=="/"):
        d=a/b
    else:
        print("Hatalı Bilgi Girdiniz")
    print("Sonuç:",d)
    f=input("Devam etmek istiyor musunuz?(e/h)?")
    if(f=="e"):
        continue
    else:
        break
print("Hesap Makinası Kapatıldı")

#--------------------------------
print()
f=1

while True:

    a=int(input("Pozitif bir sayı giriniz:"))
    if(a<=0):
        print("Pozitif bir sayı giriniz")
    else:
        for i in range(1,a+1):
            f=f*i
        print(f,"faktöriyel")
    n=input("Devam etmek istiyor musunuz ?(e/h)")
    if(n=="e"):
        continue
    else:
        break

#---------------------------------
print()
while True:
    isim = input("İsminizi girin :")
    if len(isim)<3:
        print("Tekrar girin")
    elif len(isim)>15:
        print("Tekrar girin")
    else:
        print("Hoşgeldin",isim)
        break

#------------------------------------
print()
import random
sayaç=0
while sayaç<3:
    sayi=random.randint(1,5)
    tahmin=int(input("Tahmininizi girin."))
    sayaç=sayaç+1
    if(sayi==tahmin):
        print("Tebrikler ilk seferde bildiniz.")
        break
else:
    print("Sayıyı bulamadınız.")

#-----------------------------------------
print()
i=1
while i<=9:
    print(f'{"*"*i:^9}') #f stringi '{buraya yazılan ekran çıktısı olarak alınır.}' 9 uzunluğundaki bir stringe tamamlattık ve ^ile ortalattık.
    i=i+2

print("DONE")

#---------------------------------------
print()
a="Charmander UF"
b="wassupchef0"


while(True):
    c = input("Kullanıcı Adı:")
    d = input("Şifre:")
    if ((a == c) and (b == d)):
        print("Hoşgeldiniz",a)
        break
    elif ((a != c) and (b == d)):
        print("Hatalı Kullanıcı Adı")
    elif ((a == c) and (b != d)):
        print("Hatalı Şifre")
        print("Şifrenizi Değiştirmek İster misiniz ? (E/H)")
        e=input("")
        if(e=="E"):
            f=input("Yeni Şifre:")
            print("Lütfen Bekleyin")
            b=f
            print("Şifre Başarıyla Değiştirildi")
    else:
        print("Tekrar Deneyiniz")