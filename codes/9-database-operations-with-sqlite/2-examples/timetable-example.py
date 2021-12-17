import sqlite3
bgln=sqlite3.connect("ders_programı.db")
db=bgln.cursor()
print(sqlite3.version)
print(sqlite3.sqlite_version)
db.execute("DROP TABLE IF EXISTS dersler")
db.execute("CREATE TABLE dersler(ders TEXT PRIMARY KEY,kredi INTEGER,saat INTEGER)")
ders=[('Fizik',5,5),("Kimya",3,4),("Biyoloji",5,4)]
db.executemany("INSERT INTO dersler VALUES (?,?,?)",ders)
db.execute("INSERT INTO dersler VALUES ('Matematik',5,7)")
db.execute("ALTER TABLE dersler RENAME TO dersler1") #tablonun ismi dersler iken dersler1 olarak değiştirldi
db.execute("UPDATE dersler1 SET ders='İngilizce' WHERE ders='Kimya'")
m=db.execute("SELECT * FROM dersler1 WHERE ders LIKE 'M%'") #M ile başlayanların listsini döndürür
for mbaslayan in m:
    print(mbaslayan)
    print()
d=db.execute("SELECT ders FROM dersler1") #derslerin listesini verir
for dler in d:
    print(dler)
    print()
#db.execute("SELECT DISTINCT ders FROM dersler1 WHERE ders LIKE 'M%'") #dersler1 tablosundaki adı m ile başlayan ders alanındaki kayıtları tekrarsız listeler
k=db.execute("SELECT * FROM dersler1 WHERE kredi=5") #dersler1 tablosunda kredisi 5 olan tüm kayıtları listeler
for kredi_ in k:
    print(kredi_)
    print()
s=db.execute("SELECT * FROM dersler1 ORDER BY saat DESC") #dersler1 tablosunundaki derslerin saatlerine göre azalan sırada listeler
for d_saat in s:
    print(d_saat)
    print()
db.execute("DELETE FROM dersler1 WHERE ders='İngilizce'") #ingilizceyi dersler1 tablosundan siler
db.execute("UPDATE dersler1 SET ders='Edebiyat' WHERE ders='Fizik'") #fizik dersinin adını edebiyat olarakdeğiştirdik
db.execute("INSERT INTO dersler1 (ders,kredi,saat) VALUES ('Coğrafya',2,3)") #coğrafya dersini tabloya ekledik
#db.execute("DROP TABLE if exists dersler1") ## dersler1 tablosunu siler
for kyt in db.execute("SELECT * FROM dersler1"):
    for i in kyt:
        print(i,":",end="")
    print("")
bgln.commit()
bgln.close()