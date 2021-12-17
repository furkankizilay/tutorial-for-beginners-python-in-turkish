"""
eğer sınıf içinde tanımlayacağınız fonksiyon herhangi bir
örnek ya da sınıf niteliği üzerinde herhangi bir işlem yapmayacaksa şöyle bir şey yazabilirsiniz:

"""

class Sınıf():
    sınıf_niteliği = 0

    def __init__(self, veri):
        self.veri = veri

    def örnek_metodu(self):
        return self.veri

    @classmethod
    def sınıf_metodu(cls):
        return cls.sınıf_niteliği

    @staticmethod
    def statik_metot():
        print('merhaba statik metot!')