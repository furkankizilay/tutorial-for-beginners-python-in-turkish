# Programlamaya Giriş :

**Algoritma** ; herhangi bir problemin çözümü için izlenecek yol.

-	Açık seçik olmalı
-	Yürütülebilir olmalı
-	Sıralı olmalı
-	Sonlu bir zamanda yürütülebilir olmaldır.

Algoritmada yer alan her bir emire **KOMUT** denir.
Algoritma, bir problemi çözüm basamaklarına ayırma işlemi olup, çözümü bilgisayar ortamında yapılabilmesi için o algoritmanın bir program halinde sunulması gerekir.

**Algoritmayı sunum (presentation) şekilleri;**

*	Metinsel düz ifade ( konuşma dili)
*	Pseudo Cod ( sözde kod ) ( kaba kod)
*	Flowcards ( akış şemaları)

## Bilgisayar ve Bileşenleri

* **Hardware ( donanım ) :**

    - Giriş Birimleri
    - Çıkış Birimleri
    - Mikroişlemci(CPU/işlemci) : Aritmetik işlemlerin yapıldığı, yapılan işlemlerin denetlendiği / yönlendirildiği bölümdür.
    - Hafıza Birimleri(RAM/ROM Bellek) : Bilgisayarın üzerinde çalıştığı verilerin sürekli veya geçici olarak depolandığı yerdir.
    - Depolama Birimleri (Hard disk, Flash disk)  : Verilerin kalıcı olarak depolandığı bölümdür.

* **Software ( Yazılım ) :**   

    - Sistem Yazılımları : Temelde bilgisayarı çalıştıran ve donanımların birbirleriyle iletişimini sağlayan yazılımdır.

    - Uygulamaya Yazılımları : Programcının bir problemin çözümü için herhangi bir programlama dili ile yazdığı programlardır. Kullanıcıların amacına göre bilgisayara yüklenen ve işletim sistemi tarafından çalıştırılan yazılımlardır.

## Yazılım ve Donanım Arasındaki İlişki


**Compiler ( derleyici ) ve Interpreter ( yorumlayıcı ) ;**

Bilgisayara ne yapması gerektiğini söyleyen bir komuta ( emire ) program, bu komutları veren kişiye programcı, komutların bütününe ise programlama dili denir.
Yazdığımız programları makine diline çeviren, makine dilinde elde edilen sonuçları bizim anladığımız şekle çeviren programlama çevirici ( derleyici veya yorumlayıcı ) program denir.


* **Compiler ( Derleyici ) ;** Derleyicilerin görevi herhangi bir programlama dili ile yazılmış bir programı ( yani kaynak kodu ), makine diline çevirmektedir.

* **Interpreter ( Yorumlayıcı ) ;** Yorumlayıcıların görevi, bir programlama dilinde kodlanmış bir kaynak programı, ilk satırından son satırına kadar satır-satır inceleyerek varsa hataları düzeltmek ve çalıştırmaktır.


**Compiler ve Interpreter Arasındaki Farklar :**

Derleyici programın tamamını kontrol eder bir satırında hata varsa program satırları bittikten sonra hatayı gösterir. Yani kaynak kodu bir defa çevirir. Interpreter ise programın bir yerinde hata varsa çalışırken hatalı satırlara geldiğinde durur ve hata mesajı verir. Hata düzeldikten sonra tekrar birinci satırdan itibaren kodu çevirir.

## Source Program ( Kaynak Program) 

Herhangi bir programlama dili ile yazılmış ham, derlenmemiş programa Source Program denir. Python’da Source Program dosyasının uzantısı .py'dir.

## Executable File ( Çalıştırılabilir Dosya )

Bir programlama dilinde yazılmış source programın derlenmesi ile elde edilen, makine diline dönüştürülmüş ve çalışmaya hazır programlara denir. Dosya uzantısı ".exe." dır.

## Interpreter of Python

Python, Java gibi hem compiler ve ınterpreter tekniğini bir arada kullanır.
*	Python editöründe yazılmış bir source kod( .py uzantılı dosya) bytecode compilerından geçirilir.
*	Bu kodla ilgili kütüphane modülleri ( .pyc uzantılı dosyalar) import edilerek virtual machine ( sanal makine ) kodu, çalıştırılabilir kod ( makine dili ) formatına dönüştürülür. 

Bytcode derleyicisi, source code ( python komutarını ) girdi olarak kabul eder. Ardından çıktı olarak makine tarafından okunabilecek Python bayt kodunu ( .pyc uzantılı dosya) üretir.

Sanal makine ise girdi olarak Python bayt kodunu ( .pyc uzantılı ) ve varsa ilgili kütüphane modüllerini alır, bytcode ile temsil edilen makine talimatlarını çalıştırır, yani çalıştırılabilir (.exe) dosya formatına dönüştürür. 
Python'da bir kütüphane modülünü mevcut kaynak dosyasına eklemek/aktarmak için import deyimi kullanılır.

## Programlama Dilleri

1. Assembly dili ( Alt seviyeli diller )
2. Yüksek seviyeli diller

İnsanların algılamasına yakın diller *yüksek seviyeli* dillerdir makine/bilgisayara yakın diller *assembly diller* olarak adlandırılır.

## Python Editöreleri

Bir programlama dili ile kod yazmak, derlemek, çalıştırmak. hataları ayıklamak için kısaca IDLE ( Integrated Development Environment-Entegre Yazılım Geliştime Ortamı) adı verilen editörler kullanılır. Resmi python editörü IDLE harici PyDev, PyCharm gibi birçok farklı editör geliştirilmiştir. 

Python geniş ve açık kaynaklı komut isteminden grafiksel uygulamalara (GUI), veri madenciliğinden veri analizine, robot programlamadan ağ programlamaya bir kütüphaneye sahiptir. Python dili ile konsol uygulamaları, görsel masaüstü (GUI) uygulamaları, web tabanlı uygulamalar gerçekleştirilebilir.

