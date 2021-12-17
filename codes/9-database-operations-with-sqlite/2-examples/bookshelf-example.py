import sqlite3
con=sqlite3.connect("bk.db")  # Tabloya bağlanıyoruz
cursor=con.cursor() # veri tabanı üzerinde işlem yapmak için imleç oluşturuyoruz
def tablo_olustur():
    cursor.execute("create table if not exists yenik (İsim text, Yazar text, Yayınevi text, Sayfa_sayısı text)")
    con.commit() # veri tabanına hafızadaki bilgiyi kaydeder
def deger_ekle():
    cursor.execute("insert into yenik values('İstanbul Hatırası', 'Ahmet Ümit','Everest',561)")
    cursor.execute("insert into yenik values('Tehlikeli Oyunlar', 'Oğuz Atay', 'İletişim',479)")
    cursor.execute("insert into yenik values('Kürk Mantolu Madonna','Sabahattin Ali','Yapı Kredi',160)")
    con.commit() ## veri tabanına hafızadaki bilgiyi kaydeder
def deger_ekle2(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("insert into yenik values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()
isim=input("İsim:")
yazar=input("Yazar:")
yayınevi=input(("Yayınevi:"))
sayfa_sayısı=int(input("Sayfa sayısı:"))
def veri_al():
    cursor.execute("select * from yenik")  # Bütün bilgileri alıyoruz.
    data=cursor.fetchall() # Veritabanından bilgileri çekmek için fetchall() kullanıyoruz.
    print("Kitaplık tablosunun bilgileri :")
    for i in data:
        print(i)
    #con.commit() işlemine gerek yok çünkü tabloda herhangi bir değişkik yapmadık
def veri_al2():
    cursor.execute("select İsim, Yazar from yenik") # Sadece İsim ve Yazar özelliklerini alıyoruz.
    data=cursor.fetchall()
    print("Kitaplık tablosunun bilgileri :")
    for i in data:
        print(i)
def veri_al3(Yayınevi):
    cursor.execute("select * from yenik where Yayınevi =?",(Yayınevi,))
    data=cursor.fetchall()
    print("Kitaplık tablosu bilgileri :")
    for i in data:
        print(i)
def veri_guncelle():
    cursor.execute("update yenik set Yayınevi='Doğan Kitap' where Yayınevi='Everest'")
    con.commit()
def veri_sil(yazar):
    cursor.execute("delete from yenik where Yazar=?",(yazar,))
    con.commit()
tablo_olustur()
deger_ekle()
deger_ekle2(isim,yazar,yayınevi,sayfa_sayısı)
veri_al()
veri_al2()
veri_al3("Everest")
veri_guncelle()
veri_al()
veri_sil("Ahmet Ümit")
veri_al()
con.close()