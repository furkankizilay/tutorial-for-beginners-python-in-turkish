class Giriş():
    def __init__(self, mesaj='Müşteri numaranız: '):
        cevap = input(mesaj)
        print('Hoşgeldiniz!')

    @classmethod
    def paroladan(cls):
        mesaj = 'Lütfen parolanızı giriniz: '
        cls(mesaj)

    @classmethod
    def tcknden(cls):
        mesaj = 'Lütfen TC kimlik numaranızı giriniz: '
        cls(mesaj)

Giriş.tcknden()