import sys
#print(dir(sys))
#a=int(input("a:"))
#b=int(input("b:"))
#sys.exit()
#c=int(input("c:")) #c çalışmadı çünkü ykarıda programdan çıktık

#stderr ve stdout

#Bilgisayarlar uygulamalarımız ve işlemlerimiz çalıştığı zaman çıktı vermek ve girdi almak için şu dosyaları kullanır.
#stdin : Bu standard dosya, işlemimizin (process ) kullanıcıdan input almasını sağlar.
#stdout : Bu standard dosya, işlemimizin (process ) çıktı vermesini sağlar.
#stderr : Bu standard dosya, işlemimizin hata mesajlarını çıktı olarak vermek için kullanılır.

#Biz print() fonksiyonumuzu kullandığımızda aslında standard olarak stdout kullanılmaktadır. Ancak biz istersek *stderr'e de bir şeyler yazabiliriz.

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
if len(sys.argv)==4: #1 elemanda dosaynın kendisi
    print("Kök Bulma",kok_bulma(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
else:
    sys.stderr.write("Lütfen doğru değerler girin.")
    sys.stderr.flush()