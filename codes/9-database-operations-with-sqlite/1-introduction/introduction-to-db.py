# Bütün ilişkisel veritabanlarında olduğu gibi, Sqlite da bu verileri tablo benzeri bir yapı içinde tutar.
# Sqlite ile bir tablo oluştururken, bu tabloya bir de ad vermemiz gerekir.
# vt = sqlite3.connect('veritabanı_adı')
# deneme.sqlite adını verdiğimiz bir veritabanı dosyasına, connect() metodu yardımıyla bağlandık.
# connect() metoduna verdiğimiz varitabanı_adı adlı argüman, kullanacağımız veritabanının adıdır.
# Eğer bu komutu verdiğiniz dizin içinde deneme.sqlite adlı bir veritabanı yoksa, bu ada sahip bir veritabanı oluşturulacaktır. Eğer zaten bu adla bir veritabanı dosyanız varsa, sqlite3 bu veritabanına bağlanacaktır.
# connect() metoduna argüman olarak tam dosya yolu da verilebilir.
# vt = sqlite3.connect('c:/users/fozgul/desktop/test.sqlite') #Windows
#sqlite3 ile geçici bir veritabanı da oluşturabilirsiniz.
# vt = sqlite3.connect(':memory:') # RAM üzerinde çalışır.
# vt = sqlite3.connect('') # Sabit disk üzerinde çalışır.
# Sqlite, veritabanını o anda içinde bulunduğunuz dizin içinde oluşturuyor. Mesela MySQL kullanıyor olsaydınız, oluşturulan veritabanlarının önceden tanımlanmış bir dizin içine atıldığını görecektiniz.
# Veritabanını oluşturduktan veya varolan bir veritabanı ile bağlantı kurduktan sonra, veritabanı üzerinde işlem yapabilmek için sonraki adımda bir imleç oluşturmamız gerekir.
# İmleç oluşturmak için cursor() adlı bir metottan yararlanacağız:
# im = vt.cursor()
# İmleci oluşturduktan sonra artık önümüz iyice açılıyor. Böylece, yukarıda oluşturduğumuz im nesnesinin execute() metodunu kullanarak SQL komutlarını çalıştırabileceğiz.
# eğer tablo adı ve sütun başlıklarında birden fazla kelimeden oluşan etiketler kullanacaksanız bunları ya birbirine bitiştirin ya da tırnak içine alın.
import sqlite3

vt = sqlite3.connect('perso.sqlite')
im = vt.cursor()

im.execute("""CREATE TABLE 'personel dosyasi'
('personel ismi', 'personel soyismi', memleket)""")

# aynı kodları ikinci kez çalıştırdığınızda şöyle bir hata mesajı ile karşılaşacaksınız:
# sqlite3.OperationalError: table personel already exists, bu hatayı almamak için tabloyu oluştururken CREATE TABLE IF NOT EXİSTS komutu yazılır.
# im.execute("""INSERT INTO personel VALUES ("Fırat", "Özgül", "Adana")""")
# Biz henüz sadece verileri girdik. Ama verileri veritabanına işlemedik. Bu girdiğimiz verileri veritabanına işleyebilmek için commit() adlı bir metottan yararlanacağız:
# vt.commit()
# Bir veritabanı üzerinde yapacağımız bütün işlemleri tamamladıktan sonra, prensip olarak, o veritabanını kapatmamız gerekir.
# vt.close()
# çoğu durumda veritabanına girilecek veriler harici kaynaklardan gelecektir. Basit bir örnek verelim:
import sqlite3

with sqlite3.connect('vt.sqlite') as vt:
    im = vt.cursor()

    veriler = [('Fırat', 'Özgül', 'Adana'),
               ('Ahmet', 'Söz', 'Bolvadin'),
               ('Veli', 'Göz', 'İskenderun'),
               ('Mehmet', 'Öz', 'Kilis')]

    im.execute("""CREATE TABLE IF NOT EXISTS personel
        (isim, soyisim, memleket)""")

    for veri in veriler:
        im.execute("""INSERT INTO personel VALUES
            (?, ?, ?)""", veri)

    vt.commit()

# Veritabanından herhangi bir veri alabilmek için ilk olarak SELECT veri FROM tablo_adı adlı bir SQL komutundan yararlanarak ilgili verileri seçmemiz gerekiyor.
# im.execute("""SELECT * FROM faturalar""")
# SELECT * FROM faturalar ifadesi şu anlama gelir: “faturalar adlı tablodaki bütün öğeleri seç!”
# Verileri seçtiğimize göre, artık seçtiğimiz bu verileri nasıl alacağımıza bakabiliriz. Bunun için de fetchone(), fetchall() veya fetchmany() adlı metotlardan ya da for döngüsünden yararlanacağız.

import sqlite3

vt = sqlite3.connect('vt.sqlite')

im = vt.cursor()

im.execute("""CREATE TABLE IF NOT EXISTS faturalar
(fatura, miktar, ilk_odeme_tarihi, son_odeme_tarihi)""")

im.execute("""INSERT INTO faturalar VALUES
("Elektrik", 45, "23 Ocak 2010", "30 Ocak 2010")""")

vt.commit()

im.execute("""SELECT * FROM faturalar""")

veriler = im.fetchall()

print(veriler)

#SELECT * FROM faturalar komutu ‘faturalar’ adlı tablodaki bütün verileri seçiyordu. fetchall() metodu ise seçilen bu verileri alma işlevi görüyor. Yukarıda biz fetchall() metoduyla aldığımız bütün verileri veriler adlı bir değişkene atadık.
# Peki eğer siz bir veritabanı dosyasına verilerin yalnızca bir kez yazılmasını istiyorsanız ne yapacaksınız?

import sqlite3, os

dosya = 'vt.sqlite'
dosya_mevcut = os.path.exists(dosya)

vt = sqlite3.connect(dosya)
im = vt.cursor()

im.execute("""CREATE TABLE IF NOT EXISTS faturalar
(fatura, miktar, ilk_odeme_tarihi, son_odeme_tarihi)""")

if not dosya_mevcut:
    im.execute("""INSERT INTO faturalar VALUES
    ("Elektrik", 45, "23 Ocak 2010", "30 Ocak 2010")""")
    vt.commit()

im.execute("""SELECT * FROM faturalar""")

veriler = im.fetchall()
print(veriler)

# fetchone() metodu, bir veritabanından seçilen verilerin tek tek alınabilmesine izin verir.
#fetchmany() Metodu, bir veritabanından seçtiğiniz verilerin istediğiniz kadarını alabilmenize imkan tanır. # im.fetchmany(5)
#SELECT * FROM tablo_adı WHERE sütun_başlığı = aranan_veri, bu sorguyu gerçekleştirebilmek için tablodaki sütun başlıklarını bilmemiz gerekiyor.

import sqlite3

db = sqlite3.connect("vt.sqlite")

im = db.cursor()

im.execute("""CREATE TABLE IF NOT EXISTS kullanicilar
    (kullanici_adi, parola)""")

veriler = [
            ("ahmet123", "12345678"),
            ("mehmet321", "87654321"),
            ("selin456", "123123123")
          ]

for i in veriler:
    im.execute("""INSERT INTO kullanicilar VALUES (?, ?)""", i)

db.commit()

kull = input("Kullanıcı adınız: ")
paro = input("Parolanız: ")

im.execute("""SELECT * FROM kullanicilar WHERE
kullanici_adi = ? AND parola = ?""", (kull, paro))

data = im.fetchone()

if data:
    print("Programa hoşgeldin {}!".format(data[0]))
else:
    print("Parola veya kullanıcı adı yanlış!")
