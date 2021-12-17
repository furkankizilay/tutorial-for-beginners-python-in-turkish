import os

print(os.getcwd()) # Os.getcwd (), programın geçerli çalışma dizinini döndürür. Varsayılan olarak, geçerli çalışma dizini python programının dosya yoludur.

#os.chdir("D://") # Os.chdir, programın geçerli çalışma dizinini değiştirir. Aşağıdaki örnek, mevcut çalışma dizinini D sürücüsü olarak değiştirir.
#print(os.getcwd()) = D:\Users\ACER\PycharmProjects\pythonProject1\venv\Include

#os.mkdir("C://Users/Default/Newfolder") # Os.mkdir işlevi, belirtilen bir dosya yolunun boş bir dizinini oluşturur. Bu örnekteki nihai sonuç, temelde "C: / Users / Default" dosya yolunda yeni bir klasör olacaktır.
#os.mkdir("Deneme1")
#os.makedirs("Deneme2/Deneme3")
#os.rmdir("Deneme2/Deneme3") #Deneme2'nin altındaki Deneme3'ü sildik
#os.removedirs("Deneme2/Deneme3") #Deneme2'Yi ve Deneme3'ü aynı anda sildik
print(os.listdir("C://Users")) #Os.listdir işlevi, belirli bir dizindeki her bir dosyanın ve klasörün içeriğini listeler.

#Os.walk, bir dizindeki tüm klasörler ve alt klasörler arasında dolaşır. Bu işlev, bilgisayarınızda dosya ararken kullanışlıdır.
#Os.walk işlevi üç değer döndürür. Bir klasörün dosya yolu, içindeki alt klasörlerin adları ve alt klasörler içindeki dosyaların adları.

#for folder, subfolders, files in os.walk("C:\\Users"):
    #print(folder)
    #for subfolders in subfolders:
        #print(subfolders)
    #for file in files:
        #print(file)

#print(os.walk("C:/Users/user/Desktop")) #generatör döndürür
#for i in (os.walk("C:/Users/user/Desktop")): #masaüstündeki tüm dosya ve klasörleri döndürür.
    #print(i)

#for klasör_yolu,klasör_isimleri,dosya_isimleri in (os.walk("C:/Users/user/Desktop")):
#    for i in dosya_isimleri: #sadece dosya isimleri ekrana yazıldı
#        if (i.endswith(".txt")): #sadece txt olan dosya isimleri yazıldı
#            print(i)

#OS library has the ability to open files to read and write data to them. The default mode is the read state, denoted by ‘r’. The other state is the write file, denoted by ‘w’. The os.popen() takes 2 parameters. The first is the name of the file to be read/written to, and the second is the mode.

#File = popen("NewFile.txt", 'w')
#File.write("Hello World")
#File.close

#File = popen("NewFile.txt", 'r')
#print(File.read())
#File.close

#os.close()
#Bir dosyayı okuma ve yazma amacıyla açtığınızda, os.close () işlevini kullanarak kapatmanız gerekir.

#os.rename()

#Os.rename işlevi iki parametre alır. İlki, adı değiştirilecek dosyanın dosya yoludur. İkincisi, eski dosya adının değiştirilmesini istediğiniz yeni addır.
#os.rename("Old.txt","New.txt")
#os.rename("test.txt","test2.txt")

#print(os.stat("test2.txt")) #test2.txt dosyasının bilgisayrda buluan bütün özelliklerini döndürür.
#print(os.stat("test2.txt").st_mtime) #sadece st_mtime özelliğini geri döndürür.

#os.getlogin()

#The os.getlogin() functions returns the name of the user logged in on the controlling terminal of the process

user_name = os.getlogin()
print(user_name)






