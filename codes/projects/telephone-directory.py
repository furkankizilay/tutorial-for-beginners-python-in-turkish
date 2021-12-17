print('<<telefon rehberi porgramimiza hosgeldiniz>> ')
isimlistesi=[]
soyisimlistes=[]
numaralistesi=[]
say=0

def menu():
    print(F"{'>>menu<<':^10}")
    print('1.kayit ekle')
    print('2.kayit ara')
    print('3.kayit sil')
    print('4.kayitlari listele')
    print('5.cikis')

while True:
    try:
        menu()
        girilen_deger=input('seciminiz: ')
        if girilen_deger=='5':
            print('cikisiniz tamamlanmistir')
            break
        if girilen_deger=='1':
            ad=input('isim: ')
            soyad=input('Soyisim:')
            numara=int(input('numara: '))
            isimlistesi.append(ad)
            soyisimlistes.append(soyad)
            numaralistesi.append(numara)
            print(f"kayit basarili\n{'isim':^10}{'soyisim':^10}{'Numara':^10}\n{isimlistesi[say]:^10} {soyisimlistes[say]:^10} {numaralistesi[say]:^10}")
            say +=1

        if girilen_deger=="2":
            search=input('aranacak kelime giriniz: ')
            if search in isimlistesi:
                index=isimlistesi.index(search)
                print(F"aradiginiz kisi->> {isimlistesi[index]} {soyisimlistes[index]} {numaralistesi[index]}")
            if search in soyisimlistes:
                syindex=soyisimlistes.index(search)
                print(F"aradiginiz kisi->> {isimlistesi[syindex]} {soyisimlistes[syindex]} {numaralistesi[syindex]}")
            if search in numaralistesi:
                nmbr=numaralistesi.index(search)
                print(F"aradiginiz kisi->> {isimlistesi[nmbr]} {soyisimlistes[nmbr]} {numaralistesi[nmbr]}")
            if search not in isimlistesi  and search not in soyisimlistes and search  not in numaralistesi:
                print('giridiginiz islem listede bulnumamaktadir')

        if girilen_deger=='3':
            print('<<silmek icin bir kisi arayiniz>>')
            sil = input('aranacak kelimeyi giriniz: ')
            if sil in isimlistesi or sil in soyisimlistes or sil in numaralistesi:
                while True:
                    sor = input('silmek icin eminmisiniz? (E/H) ')
                    if sor.upper() == "E" or sor.upper() == "H":
                        break
                    else:
                        print('lutfen cevabinizi dogru secin')
                if sor.upper()=="E":
                    if sil in isimlistesi:
                        removeisim =isimlistesi.index(sil)
                        isimlistesi.remove(isimlistesi[removeisim])
                        soyisimlistes.remove(soyisimlistes[removeisim])
                        numaralistesi.remove(numaralistesi[removeisim])
                        print('silme islmei basarili')
                        continue

                    if sil in soyisimlistes:
                        removeisim1 = soyisimlistes.index(sil)
                        isimlistesi.remove(isimlistesi[removeisim1])
                        soyisimlistes.remove(soyisimlistes[removeisim1])
                        numaralistesi.remove(numaralistesi[removeisim1])
                        print('silme islmei basarili')
                        continue

                    if sil in numaralistesi:
                        removeisim2 = numaralistesi.index(sil)
                        isimlistesi.remove(isimlistesi[removeisim2])
                        soyisimlistes.remove(soyisimlistes[removeisim2])
                        numaralistesi.remove(numaralistesi[removeisim2])
                        print('silme islmei basarili')
                        continue

                    if sil not in isimlistesi and sil not in soyisimlistes and sil not in numaralistesi:
                        print('giridiginiz islem listede bulnumamaktadir')

                if sor.upper()=="H":
                    print('silme islemi iptal edildi')
                    continue

            else:
                print("silmek istediginiz kisi listede bulunmamaktadir")

        if girilen_deger=='4':
            print(f"{'kayit listesi':^30}")
            print(F"{'isim':^10}{'soyisim':^10}{'numara':^14}")
            for x in range( 0 , say):
                print(F"{isimlistesi[x]:^10}{soyisimlistes[x]:^10}{numaralistesi[x]:^14}")
        if girilen_deger !="1" and girilen_deger !='2' and girilen_deger !="3" and girilen_deger !="4" and girilen_deger !="5":
            print('lufen menuden bir islem giriniz ')
            continue

    except:
        print('\ndogru bir deger girmediniz \n')
