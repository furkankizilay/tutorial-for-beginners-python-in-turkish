import sqlite3 #sqlite modülü çağrıldı
print("SQLite databese sürümü : ", sqlite3.version)
print("SQLite3 kütüphane sürümü : ", sqlite3.sqlite_version)
bgln=sqlite3.connect("personel.db") #personel.db adlı database tanımlandı
imlec=bgln.cursor() #cursor nesnesi tanımlandı
imlec.execute("drop table if exists perTablo;") #Eğer perTablo önceden oluşturulduysa silinsin
imlec.execute("CREATE TABLE perTablo (no INTEGER PRIMARY KEY, ad TEXT, adres TEXT)") #perTablo isimli tablo oluşturuldu
kayitlar=[(1,"Zehra","Tokat"),(2,"Levent","İstanbul")]
imlec.executemany("INSERT INTO perTablo VALUES (?,?,?)",kayitlar) #kayitlar listesini perTabloya ekle
imlec.execute("INSERT INTO perTablo VALUES (3,'Bade','Sakarya')")
bgln.commit() #database güncellendi
print("personel.db içindeki perTablo kayıtları ad'a göre listelendi.")
for kyt in imlec.execute("SELECT * FROM perTablo ORDER BY ad"):
    print(kyt)
bgln.close() #database kapatıldı

#--------------------------------

import sqlite3
bgln=sqlite3.connect("personel.db")
vt=bgln.cursor()
#sorgu1: Adı Levent olan kaydı Bülent olarak güncelle
sorgu1=vt.execute("update perTablo set ad='Bülent' where ad='Levent'")
#sorgu2:Adı B ilebaşlayan tüm kayırları listele
sorgu2=vt.execute("SELECT*FROM perTablo Where ad LIKE 'B%'")
for kayitlar in sorgu2:
    print(kayitlar)
bgln.commit()
bgln.close()

#---------------------------------
import sqlite3
bgln=sqlite3.connect("personel.db")
vt=bgln.cursor()
#Eğer perTablo önceden oluşturulduysa silinsin
vt.execute("drop table if exists perTablo;")
vt.execute("CREATE TABLE perTablo (no INTEGER PRIMARY KEY, ad TEXT, adres TEXT)")
kayitlar=[(1,"Zehra","Tokat"),(2,"Levent","İstanbul"),(3,"Erkan","Eskişehir")]
vt.executemany("INSERT INTO perTablo VALUES(?,?,?)",kayitlar)
vt.execute("ALTER TABLE perTablo RENAME TO insanlar;") #tablonun ismi değiştirldi
vt.execute("DELETE FROM insanlar WHERE no=3;") #listeden no'su 3 olanları sil
sorgu2=vt.execute("SELECT ad,adres FROM insanlar")
for kayitlar in sorgu2:
    print(kayitlar)
bgln.commit()
bgln.close()

