class HarfSayacı :
    def __init__(self):
        self.sesli_harfler = "aeıioöuü"
        self.sessiz_harfler = 'bcçdfgğhjklmnprsştvyz'
        self.sayaç_sesli = 0
        self.sayaç_sessiz = 0
    def kelime_sor(self):
        return input("Bir kelime giriniz :")
    def seslidir(self,harf):
        return harf in self.sesli_harfler
    def sessizdir(self,harf):
        return harf in self.sessiz_harfler
    def artır(self):
        for harf in self.kelime :
            if self.seslidir(harf) :
                self.sayaç_sesli += 1
            if self.sessizdir(harf) :
                self.sayaç_sessiz += 1
        return self.sayaç_sesli,self.sayaç_sessiz
    def ekrana_bas(self):
        mesaj = "{} kelimesinde {} tane sesli {} tane sessiz harf vardır."
        sesli,sessiz = self.artır()
        print(mesaj.format(self.kelime,sesli,sessiz))
    def calistir(self):
        self.kelime = self.kelime_sor()
        self.ekrana_bas()

if __name__ == "__main__" :
    sayaç = HarfSayacı()
    sayaç.calistir()