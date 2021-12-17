import os
from datetime import datetime #stat daha anlaşılır okunsun diye ekledik
print(dir(os))
#os.chdir("C:/Users/user/Desktop") #dosyanın yerini değiştiridik
print(os.getcwd()) #dosyanın nerede olduğunu döndürür.
print(os.listdir) #şuanda bulunduğu dosyaları ve klasörleri sıralar ve geri döndürür.
#os.mkdir("Deneme1") #Yeni klasör oluşturur.
#os.makedirs("Deneme2/Deneme3") #Deneme2 klasörünü oluşturdu ve onun alrında denem3 klasörünü oluşturdu
#os.rmdir("Deneme2/Deneme3") #Deneme2'nin altındaki Deneme3'ü sildik
#os.mkdir("Deneme2/Deneme3") #Tekrar denem2'nin altında Deneme3 klasörü oluşturduk
#os.rmdir("Deneme1") #Deneme1'i sildik
#os.removedirs("Deneme2/Deneme3") #Deneme2'Yi ve Deneme3'ü aynı anda sildik
#os.rename("test.txt","test2.txt") # dosyanın adını değiştiridk
#print(os.stat("test2.txt")) #test2.txt dosyasının bilgisayrda buluan bütün özelliklerini döndürür.
#print(os.stat("test2.txt").st_mtime) #sadece st_mtime özelliğini geri döndürür.
#print(datetime.fromtimestamp(os.stat("test2.txt").st_mtime)) #st_mtime özelliğini daha anlaşılır geri döndürür.
#print(os.walk("C:/Users/user/Desktop")) #generatör döndürür
#for i in (os.walk("C:/Users/user/Desktop")): #masaüstündeki tüm dosya ve klasörleri döndürür.
    #print(i)
#for klasör_yolu,klasör_isimleri,dosya_isimleri in (os.walk("C:/Users/user/Desktop")): #daha okunur ekran çıktısı almaak için yaptık.
#    print("Klasör Yolu",klasör_yolu)
#    print("Klasör İsimleri",klasör_isimleri)
#    print("Dosya İsimleri",dosya_isimleri)
#for klasör_yolu,klasör_isimleri,dosya_isimleri in (os.walk("C:/Users/user/Desktop")):
#    for i in dosya_isimleri: #sadece dosya isimleri ekrana yazıldı
#        print(i)
#for klasör_yolu,klasör_isimleri,dosya_isimleri in (os.walk("C:/Users/user/Desktop")):
#    for i in dosya_isimleri: #sadece dosya isimleri ekrana yazıldı
#        if (i.endswith(".txt")): #sadece txt olan dosya isimleri yazıldı
#            print(i)






