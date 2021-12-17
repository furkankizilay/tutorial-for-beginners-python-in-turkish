import random
secenek=["taş","kağıt","makas"]
taş=secenek[0]
kağıt=secenek[1]
makas=secenek[2]
print("Taş,Kağıt, Makas oyununa hoş geldiniz. Oyunu bitirmek için 'q' tuşuna basınız.")
while True:
    secim = input("Taş mı kağıt mı makas mı? ")
    bil_secim = random.choice(secenek)
    if secim==taş:
        if bil_secim==taş:
            print("Bilgisayarın seçimi: Taş Sonuç: Berabere")
        elif bil_secim==kağıt:
            print("Bilgisayarın seçimi: Kağıt Kaybettiniz")
        else:
            print("Bilgisayarın seçimi: makas Sonuç: Kazandınız")
    if secim==kağıt:
        if bil_secim==taş:
            print("Bilgisayarın seçimi: Taşn Sonuç: Kazandınız")
        elif bil_secim==kağıt:
            print("Bilgisayarın seçimi: Kağıt Sonuç: Berabere")
        else:
            print("Bilgisayarın seçimi: makas Sonuç: Kaybettiniz")
    if secim==makas:
        if bil_secim==taş:
            print("Bilgisayarın seçimi: Taş Sonuç: Kaybettiniz")
        elif bil_secim==kağıt:
            print("Bilgisayarın seçimi: Kağıt Sonuç: Kazandınız")
        else:
            print("Bilgisayarın seçimi: makas Sonuç: Berabere")
        if secim=='q':
            print("Çıkılıyor...")
            break