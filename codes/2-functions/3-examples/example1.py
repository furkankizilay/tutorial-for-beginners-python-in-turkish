# Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).

def mukemmelsayi(sayi) :
    toplam = 0
    for i in range(1,sayi) :
        if (sayi % i == 0) :
            toplam += i
    return toplam == sayi

for i in range(1,1001):
    if(mukemmelsayi(i)):
        print(i,"Mükemmel sayıdır.")


birler = ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def okunus(sayi) :
    birinci = sayi % 10
    ikinci = sayi // 10

    return onlar[ikinci] + " " + birler[birinci]

sayi = int(input("Bir sayı giriniz :"))
print(okunus(sayi))

def pisagorbulma() :
    pisagorlistesi = list()
    for i in range(1,101) :
        for j in range(1,101) :
            c = (i**2 + j**2)**0.5
            if (c == int(c)) :
                pisagorlistesi.append((i,j,int(c)))
    return pisagorlistesi

for i in pisagorbulma() :
    print(i)


