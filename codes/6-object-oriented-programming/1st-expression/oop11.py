import time
import random

class rekabet():
    def __init__(self, isim, can, saldiri_gucu, kalan_mermi):
        self.isim=isim
        self.can=can
        self.guc=saldiri_gucu
        self.kalan_mermi=kalan_mermi

    def saldir(self):
        print(self.isim, "saldırıyor!")
        harcanan_mermi=random.randrange(1,10)

        if (self.kalan_mermi <= harcanan_mermi):
            harcanan_mermi=self.kalan_mermi
            print(str(self.kalan_mermi), "mermi harcandı.")
        else:
            print(str(harcanan_mermi), "mermi harcandı.")
        self.kalan_mermi -= harcanan_mermi

        return(harcanan_mermi, self.guc)

    def vuruldu(self, harcanan_mermi, guc):
        print(self.isim, "vuruldu.\n")
        self.can -= (guc * harcanan_mermi)

    def mermi_bitti_mi(self):
        if(self.kalan_mermi<=0):
            print(self.isim, "konuşuyor: Mermim bitti! Çekiliyorum.")

            if(len(dusmanlar)==1):
                return
            dusmanlar.remove(self)

            return True
        return False

    def hayatta_mi(self):
        if(self.can<=0):
            print(self.isim, "öldü.")

            dusmanlar.remove(self)

            return True
        return False


    def print(self):
        time.sleep(2)
        print(self.isim+",", "Can: {} Saldırı gücü: {} Mermi sayısı: {}".format(self.can,self.guc,self.kalan_mermi))

    def kazanan(self):
        return self.isim

#----------------------------------------------------------------------
#----------------------------------------------------------------------



dusmanlar= []
karakter_isimleri=["Türk Askeri","Rus Askeri","Amerikan Askeri","İtalyan Askeri","Fransız Askeri"]



i=0
while(i<5):
    rastgele_isim = karakter_isimleri[i]
    rastgele_can = random.randrange(200, 350)
    rastgele_guc = random.randrange(15, 20)
    rastgele_mermi = random.randrange(15, 20)
    dusman = rekabet(rastgele_isim, rastgele_can, rastgele_guc, rastgele_mermi)
    dusmanlar.append(dusman)
    i+=1





print("Düşmanlar basılıyor...\n")
time.sleep(3)


random.shuffle(dusmanlar)
for dusman in dusmanlar:
    dusman.print()
    i+=1



print("\nDüşmanlar birbirine saldırıyor...\n")
time.sleep(3)



while(True):
    if (len(dusmanlar)==5):
        dusman1 = random.randint(0,4)  # 0 ve 4 dahil. random.randrange(0,4) yapsaydık 0 dahil olacak ama 4 olmayacaktı.
        dusman2 = random.randint(0,4)
        if (dusman2 == dusman1) or ((dusman2>dusman1) and (dusman2==4)):
            continue
        else:
            print("\n\n")
            donen_deger = dusmanlar[dusman1].saldir()  # return ile "donen_deger"e iki tane argüman atadık.
            dusmanlar[dusman2].vuruldu(donen_deger[0], donen_deger[1])
            time.sleep(2)

            dusmanlar[dusman1].mermi_bitti_mi()
            dusmanlar[dusman2].hayatta_mi()

            time.sleep(4)


    elif (len(dusmanlar) == 4 ):
        dusman1 = random.randint(0,3)
        dusman2 = random.randint(0,3)
        if (dusman2 == dusman1) or ((dusman2>dusman1) and (dusman2==3)):
            continue
        else:
            print("\n\n")
            donen_deger = dusmanlar[dusman1].saldir()  # return ile "donen_deger"e iki tane argüman atadık.
            dusmanlar[dusman2].vuruldu(donen_deger[0], donen_deger[1])
            time.sleep(2)

            dusmanlar[dusman1].mermi_bitti_mi()
            dusmanlar[dusman2].hayatta_mi()

            time.sleep(4)


    elif (len(dusmanlar) == 3 ):
        dusman1 = random.randint(0,2)
        dusman2 = random.randint(0,2)
        if (dusman2 == dusman1) or ((dusman2>dusman1) and (dusman2==2)):
            continue
        else:
            print("\n\n")
            donen_deger = dusmanlar[dusman1].saldir()  # return ile "donen_deger"e iki tane argüman atadık.
            dusmanlar[dusman2].vuruldu(donen_deger[0], donen_deger[1])
            time.sleep(2)

            dusmanlar[dusman1].mermi_bitti_mi()
            dusmanlar[dusman2].hayatta_mi()

            time.sleep(4)

    elif (len(dusmanlar) == 2 ):
        dusman1 = random.randint(0,1)
        dusman2 = random.randint(0,1)
        if (dusman2 == dusman1) or (dusman2==0):
            continue
        else:
            print("\n\n")
            donen_deger = dusmanlar[dusman1].saldir()  # return ile "donen_deger"e iki tane argüman atadık.
            dusmanlar[dusman2].vuruldu(donen_deger[0], donen_deger[1])
            time.sleep(2)

            dusmanlar[dusman2].hayatta_mi()
            dusmanlar[dusman1].mermi_bitti_mi()

            time.sleep(4)


            if(len(dusmanlar)==1):
                kazanan_dusman1=dusmanlar[0].kazanan()
                print("\nSAVAŞ BİTTİ!")
                print("Kazanan: {}".format(kazanan_dusman1))
                input()
                break



    elif (len(dusmanlar) == 1):
        kazanan_dusman2=dusmanlar[0].kazanan()
        print("\nSAVAŞ BİTTİ!")
        print("Kazanan: {}".format(kazanan_dusman2))
        input()
        break

    else:
        print("HERKES ÖLDÜ, KAZANAN YOK!")
        input()
        break