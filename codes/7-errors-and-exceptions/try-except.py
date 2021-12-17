sayı1=int(input("İlk sayıyı giriniz :"))
sayı2=int(input("İkinci sayıyı giriniz :"))
try:
    sayı1=int(sayı1)
    sayı2=int(sayı2)
    print(sayı1/sayı2)
except(ValueError,ZeroDivisionError):
    print("Bir hata oluştu")

#-------------------------------

counter=1 #döngünün kaç kez çalıştığını görmek için counter'ı atadık
while True:
    try:
        age=int(input("Yaşınızı giriniz :"))
    except ValueError: #öngörülen hata
        print("Yanlış değer girdiniz.")
    except Exception as exceptionObject: #öngörülmeyen hata
        print("Bir hata oluştu.",exceptionObject)
    else: #else try'ın hata alamdığı exceptlerin çalışmadığı durumlarda çalışır.
        print(f"{age} yaşındasınız.")
        break #yaşı bastırdık ve while true döngüsünü kırdık.
    finally: #finally her koşulda çalışır.
        print(f"Döngü {counter} defa çalıştı")
        counter+=1
        if counter>5:
            raise ValueError("Çok fazla deneme yapıldı.") #hatayı biz vermek istediğimizde kullanılır. raise if'siz de kullanılabilir.

#--------------------------------------

kat=int(input("Hangi kata çıkıcaksınız ?"))
if kat ==6:
    raise NameError("Bu kata çıkamazsınız.")
print(f"Asansör {kat}'a çıkıyor.")

#--------------------------------------

def terscevir(s):
    if (type(s) != str):
        raise ValueError("Lütfen string bir değer giriniz")
    else:
        return s[::-1]

print(terscevir("Python"))
try:
    print(terscevir(12))
except ValueError:
    print("Fonksiyon hata verdi")

#--------------------------------------
liste = ["345", "sadas", "324a", "14", "kemal"]

for eleman in liste:
    try:
        eleman = int(eleman)  # Eğer hata ile karşılaşırsak burası hata verecek ve print çalışmayacak.
        print(eleman)
    except:
        pass  # pass deyimi bir blokun hiçbir şey yapmadığı anlamına geliyor. Python'ın hata vermemesi için kullanabilirsiniz.


#----------------------------------------
class myException(Exception) :
    name = "myException.py"

class firstException(myException) :
    def __init__(self,mesaj):
        self.mesaj = mesaj

try :
    raise firstException("This is my first exception")
except firstException as exc:
    print("Exception : ",exc.mesaj)
    print("Modul :",exc.name)