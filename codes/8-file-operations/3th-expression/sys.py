import sys
#print(dir(sys))
#a=int(input("a:"))
#b=int(input("b:"))
#sys.exit()
#c=int(input("c:")) #c çalışmadı çünkü yukarıda programdan çıktık

#stderr ve stdout

#Bilgisayarlar uygulamalarımız ve işlemlerimiz çalıştığı zaman çıktı vermek ve girdi almak için şu dosyaları kullanır.
#stdin : Bu standard dosya, işlemimizin (process ) kullanıcıdan input almasını sağlar.
#stdout : Bu standard dosya, işlemimizin (process ) çıktı vermesini sağlar.
#stderr : Bu standard dosya, işlemimizin hata mesajlarını çıktı olarak vermek için kullanılır.

#Biz print() fonksiyonumuzu kullandığımızda aslında standart olarak stdout kullanılmaktadır. Ancak biz istersek *stderr'e de bir şeyler yazabiliriz.

#sys.stderr.write("Bu bir hata mesajıdır.\n")
#sys.stderr.flush() #büyük dosyalarda ekrana hemen yazak için kullanılır burda kullanmı gerekli değildi
#sys.stdout.write("Bu normal bir yazıdır.\n")
#print(sys.argv) #bilgisayardaki yerini döndürdü

for i in sys.argv: #"dosyanın_adı.py" şeklinde açılır.
    print(i)

#------------------------------
def kok_bulma(a,b,c): #alt+f12
    delta=b**2-4*a*c
    if delta<0:
        print("Reel kök yok.")
    else:
        x1=(-b-delta**0.5)/(2*a)
        x2=(-b+delta**0.5)/(2*a)
        return x1,x2
if len(sys.argv)==4: #1 elemanda dosyanın kendisi
    print("Kök Bulma",kok_bulma(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
else:
    sys.stderr.write("Lütfen doğru değerler girin.")
    sys.stderr.flush()

#---------------------------------------------------------------------------------------
import sys
print(dir(sys))
print(sys.argv) #yazdığımız program çalıştırılırken kullanılan parametreleri bir liste halinde tutar.
print(sys.executable) #Python’ın çalıştırılabilir dosyasının adını ve yolunu döndürür
print(sys.getwindowsversion()) #kullanılan Windows sürümüne ilişkin bilgi verir
print(sys.platform) # kodlarımızın çalıştığı işletim sistemi hakkında bize bilgi verir
print(sys.prefix) # Python’ın hangi dizine kurulduğunu gösterir
print(sys.version) #pthon sürümüne ilişkin ayrıntılı bilgi verir
sayi=int(input("Bir sayı giriniz :"))

if sayi<0 :
    print("sistemden çıkılıyor")
    sys.exit()
else:
    print(sayi)
#-----------------------
import sys

def çık():
    print('Çıkılıyor...')
    sys.exit()

if len(sys.argv) < 2:
    print('Gerekli parametreleri girmediniz!')
    çık()

elif len(sys.argv) > 2:
    print('Çok fazla parametre girdiniz!')
    çık()

elif sys.argv[1] in ['-v', '-V']:
    print('Program sürümü: 0.8')

else:
    mesaj = 'Girdiğiniz parametre ({}) anlaşılamadı!'
    print(mesaj.format(sys.argv[1]))
    çık()


#C:\Users\fozgul\Belgelerim> python deneme.py
#Gerekli parametreleri girmediniz!
#Çıkılıyor...

#C:\Users\fozgul\Belgelerim> python deneme.py -a
#Girdiğiniz parametre (-a) anlaşılamadı!
#Çıkılıyor...

#C:\Users\fozgul\Belgelerim> python deneme.py -a -b
#Çok fazla parametre girdiniz!
#Çıkılıyor...

#C:\Users\fozgul\Belgelerim> python deneme.py -v
#Program sürümü: 0.8

#C:\Users\fozgul\Belgelerim> python deneme.py -V
#Program sürümü: 0.8
#---------------------------------
#stdout
import sys

for i in 'istihza':
    sys.stdout.write(i+'\n')

f = open('çıktılar.txt', 'w')
print('merhaba zalim dünya', file=f)

#Burada çıktılar.txt adlı bir dosya oluşturduk ve bunu print() fonksiyonunun file parametresine atayarak,
#çıktıları komut satırı yerine çıktılar.txt adlı dosyaya gönderdik.

import sys

f = open('çıktılar.txt', 'w')
sys.stdout = f
sys.stdout.write('merhaba zalim dünya')

#yukarıdaki ile aynı işlevi yaptı

#-------------------
#stderr

f = open('çıktılar.txt', 'w')
sys.stdout = f
sys.stdout.write('merhaba zalim dünya')
#Bu kodlar, bildiğiniz gibi, çıktı olarak verilmek istenen değerlerin çıktılar.txt adlı bir dosyaya
# yönlendirilmesini sağlıyor. Ancak kodlarımızı bu şekilde yazdığımızda sadece normal değerler yönlendirilecektir. Mesela çalışma esnasında ortaya çıkan hatalar yine komut ekranına basılmaya devam edecektir:

import sys

çıktılar = open('çıktılar.txt', 'w')
hatalar = open('hatalar.txt', 'w')
sys.stdout = çıktılar
sys.stderr = hatalar

print('normal çıktı')
print('hata mesajı: ', 1/0)
#Bu kodları çalıştırdığınızda, hata mesajı üretmeden başarıyla tamamlanan çıktıların çıktılar.txt adlı dosyaya,
#hata mesajlarının ise hatalar.txt adlı dosyaya yönlendirildiğini göreceksiniz.

#-----------------------------
#stdinn

#verileri kullanıcıdan input() fonksiyonu yerine doğrudan sys.stdin niteliği aracılığıyla da alabilirsiniz
import sys
sys.stdin.read()
#Bu komutları verdiğinizde, komut satırı sizden veri almaya hazır hale gelir.
#Bu şekilde istediğiniz kadar veriyi komut satırına girebilirsiniz

#sys.stdin.read()
#sys.stdin.readline()
#sys.stdin.readlines()

#read() fonksiyonu birden fazla satır içeren verilerin girilmesine müsaade eder ve çıktı olarak bir karakter dizisi verir:
#readline() fonksiyonu tek bir satır içeren verilerin girilmesine müsaade eder ve çıktı olarak bir karakter dizisi verir:
#readlines() fonksiyonu birden fazla satır içeren verilerin girilmesine müsaade eder ve çıktı olarak bir liste verir:

import sys

f = open('oku.txt')

sys.stdin = f

while True:
    satırlar = sys.stdin.readline()
    if satırlar.strip() == ':q':
        break
    else:
        sys.stdout.write(satırlar)