n = "python öğreniyorum"
a = int((n.count(" ")))
b = a + 1
c = int((len(n) - a))
print("n'deki kelime sayısı:", b)
print("n'deki harf sayısı:", c)

#---------------------------------
print()
sayac = 0

while True:
    sifre = (input("Şifrenizi Girin:"))
    if (sifre == "elma"):
        print("Şifre doğru")
        break
    sayac += 1
    if (sayac > 3):
        print("Hakkınız doldu")
        break

#--------------------------------
print()
n = input("Bir kelime giriniz:")

if (n == "".join(reversed(n))):
    print("Palindrom")
else:
    print("Palindrom değil")

#---------------------------------
print()
n = input("Dosya ismi:")

if (n.endswith(".py")):
    print("Python dosyası")
else:
    print("Python dosyası değil")

# bir sitringi silmek için del fonksiyonu kullanılır
# stringleri dilimlemek için : operatörü kullanılır : ile birlikte köşeli parantezler kullanılır.
# stringleri biçimlendirmek için % operatörü kullanılır.Tam sayı değişkenleri için %d, string değişkenler için %s, kesirli sayı değişkenleri için %f değişkeni kullanılır.

#-------------------------------------
print()
print("Oyuncu Kaydetme Sistemi")

a=input("Oyuncu'nun Adı:")
b=input("Oyuncu'nun Soyadı:")
c=input("Oyuncu'nun Yaşı:")
d=input("Oyuncu'nun Takımı:")

print("Bilgileriniz İşleniyor")

x=[a,b,c,d]

print("Adınız:{}\nSoyadınız:{}\nYaşınız:{}\nTakımınız:{}\n".format(x[0],x[1],x[2],x[3]))

print("Bilgileriniz Kaydedildi")

#---------------------------
print() #f string
a="furkan"
b="kızılay"
c="bilgisayar mühendisi"

d=f"{a} {b} {c}'dir."
print(d)