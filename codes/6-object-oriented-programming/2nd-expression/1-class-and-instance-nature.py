class Çalışan():
    kabiliyleri = ["Sınıf niteliği"]

    def __init__(self):
        self.kabiliyleri = ["Örnek niteliği"]

#sınıf niteliğine erişmek için
#sınıf adını kullanıyoruz
print(Çalışan.kabiliyleri)

#örnek niteliğine erişmek için
#örnek adını kullanıyoruz
ahmet=Çalışan()
print(ahmet.kabiliyleri)