class calisan(): #eğer bu sınıftan yeni sınıfar türeticeksek parantez koymamaız gerekir.
    zam_oranı=1.40 #zam oranını da dışarıdan çağırabilirdik.
    per_say=0
    def __init__(self,ad,soyad,maaş): #eğer buraya eposta yazsaydım
        self.ad=ad
        self.soyad=soyad
        self.maaş=maaş
        self.eposta=self.ad+self.soyad+"@sirket.com"
        calisan.per_say=calisan.per_say+1
    def tam_ad(self):
        return "Adı: {} Soyadı: {}".format(self.ad,self.soyad)
    def arttır(self):
        #self.maaş=(self.maaş*calisan.zam_oranı)
        self.maaş=(self.maaş*self.zam_oranı)
        #self.maaş=(self.maaş*zam_oranı) hata mesajı verir çünkü zam_oranı dışarıda.

class gelistirici(calisan): #ınheritance(miras kalıtım)
    def __init__(self,ad,soyad,maaş,p_dili):
        #calisan.__init__(self,ad,soyad,maaş)
        super().__init__(ad,soyad,maaş) #multi olsaydı parantez içine hangisinden türedğini yazmamız gerekirdi.
        self.p_dili=p_dili
        self.zam_oranı=2 #geliştici için zam oranını değiştirdim

class yönetici(calisan):
    def __init__(self,ad,soyad,maaş,calısanlar=None): #liste boş gelirse hata vermesin none değerini versin diye yaptık.
        super().__init__(ad,soyad,maaş) #super miras alınan üst sınıf yapılandırıcısına çağrıda bulunur böylece üst sınıfın özellik ve metotlarında değişiklik yaparken mevcut alt sınıfın özelliklerini korumuş oluruz.
        if calısanlar is None:
            self.calısanlar=[] #eğer calısanlar'ı tanımlamadıysam liste oluştur.
        else:
            self.calısanlar=calısanlar #eğer tanımladıysam o listeye bu calısanları ekle.

    def eleman_ekle(self,eleman):  # dışarıdan yeni bir eleman ekleme
        self.calısanlar.append(eleman)

    def eleman_çıkar(self,eleman): # eleman çıkarmak için
        self.calısanlar.remove(eleman)

    def calısanlar_listele(self):
        for eleman in self.calısanlar:
            print(eleman.tam_ad())


personel1=calisan("demir","surel",3000)
personel2=calisan("koray","yıldırım",3500)

gelistirici1=gelistirici("dağra","dağ",4000,"Python")#calisanın tum özelliklerine geliştirice sahip cünkü ondan türedi.

yönetici1=yönetici("ateş","uzun",4500,[gelistirici1,personel1])



print(yönetici1.tam_ad())
print()
print(yönetici1.calısanlar_listele())
print()
yönetici1.eleman_ekle(personel2)
print(yönetici1.calısanlar_listele())
print()
yönetici1.eleman_çıkar(personel2)
print(yönetici1.calısanlar_listele())
print()
print(gelistirici1.tam_ad(),gelistirici1.p_dili,gelistirici1.maaş)
gelistirici1.arttır()
print(gelistirici1.maaş)


print(isinstance(personel2,calisan)) #personel2'nin çalışan sınıfına ait olup olmadığını sorgular.
print(isinstance(personel1,yönetici))
print(issubclass(calisan,yönetici)) #calısan yöneticinin alt sınıfı mı diye sorguladık.



