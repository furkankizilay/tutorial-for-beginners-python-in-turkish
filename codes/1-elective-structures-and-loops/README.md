## Seçimli Yapılar 

**Giriş :** Normal bir programın işleyişi, ilk satırdan son satıra doğru sırası ile adım adım gerçekleşir. Fakat bu işleyiş sırası, bir koşula bağlı olarak değiştirilebilir. Programın işleyişi sırasının bir koşula bağlı olarak değiştirilmesi işlemine *branching (şartlı dallanma)* adı verilir ve dallanma işlemini gerçekleştiriren komutlara da *karar komutları* denir. Karar yapılarında koşula (bir şarta) bağlı olarak iki ya da daha fazla seçenekten birini seçme işlemi gerçekleştirilmektedir. 

**Program :** Şarta bağlı olarak hangi işlemi yapacağına karar verir. Python'da *'if','if else',ve 'if-elif else'* olmak üzere üç adet seçme işlemini gerçekleştiren yapı vardır.

1. **if: (Tek Seçimli Yapı):** Koşula bağlı olarak tek bir işlemi yerine getiren yani branching işlemini gerçekleştiren yapıdır. Hemen hemen bütün programlama dillerinde bu işlem için if deyimi/komutu kullanılır. Eğer koşul kısmında birden çok fazla değerin karşılaştırılması yapılıcaksa mantıksal operatörler (and,or) kullanılabilir. if: sorgularonda koşuldan sonra ':' koymayı unutmamak ve büyük/küçük ayrımına dikkat etmek lazım.

    *  **Indentation (Kod Bloğu: Girinti Mekanizması) :** Programlama dillerinde kod bloklarını belirlemek için {...} süslü parantezler ya da begin ... and sözcükleri kullanılırken Python'da ise girinti mekanizması kullanılır. Python'da dikey olarak aynı hizada başlayan ardışık kod satırları bir blok kabul edilir. Pratikre her bir blok girintisi için 4 boşluk (1 tab) bırakılması tavsiye edilir.


2. **if: else: (Çift Seçimli Yapı) :** Koşula bağlı olarak iki işlem yerine getiren yani branching işlemini gerçekleştiren yapıdır. Tüm programlama dillerinde olduğu gibi Python'da da bu işlem için if/else deyimi kullanılır. if: ve else:'den sonra ':' koymak unutulmamalı. 

3. **if: elif: else: (Çok Seçimli Yapı) :** Çoklu seçimlerde if-elif deyimi merddiven basamakları şeklinde iç içe kullanılır. Koşul sayısı ikiden fazla olduğunda tercih edilir.


## Loops (Döngüler) 

Döngüler tekrar eden işlemleri gerçekleştirmek için tasarlanmış yapılardır. Bu nedenle döngü yapıları, farklı kaynaklarda tekrarlı yapılar olarak da adlandırılmaktadır. Programcı, yazdığı programın bazı kod satırlarını tekrarlı olarak çalıştırma ihtiyacı duyduğunda döngü yapılarını kullanır.

1. **while döngüleri :** Tekrar sayısının koşula bağlı olduğu yani koşul gerçekleştiği veya gerçekleşmediği sürece işlemlerin tekrar ettiği döngülerdir. Tekrar sayısı baştan bilinmediğinden, burada tekrar sayısı koşula bağlı olarak gerçekleşir.

2. **for döngüleri :** Terkarlama işlemin kaç kez yapılacağı baştan belli olduğu dögülerdir.

3. **while Döngüsü :** İşlemlerin ne kadar tekrarlanacağı baştan belli olmadığı ancak bir koşulun doğru ya da yanlış olmasına bağlı olarak tekrar sayısının belirlendiği döngülerdir.


4. **while True :** Sonsuz döngü oluşturur. Döngü içine koşulsuz giriş sağlanırken döngüden çıkış ancak break komutu ile gerçekleşir. Döngü içerisnde kod satırları hep aynı hizada (4 karakterlik (tab)) aynı girintiye sahip olmalıdır. Bir kod bloğu içerisinde baş kod bloklarıda yer alabilir fakat her yeni kod bloğu 4 karakter daha sağa hizalanmalıdır. while döngülerinde döngüden çıkışı gerçekleştiricek koşulu sağlayan bir ifade döngü içerisinde bulunmalıdır. Aksi takdirde program çıktı vermezsensiz döngüye girer (while True gibi), sonsuz döngülerden de çıkış, döngü kırılarak break komutu ile gerçekleşir.

### break ve continue Komutları 
Break ve continue komutları döngülerde ek kontrol sağlar. break komutu; bir koşula bağlı olarak döngü değişkeninin son değerine ulaşmadan döngüyü terk etmesini sağlar. continue komutu ise döngü içerisinde o anki işlemi atlayarak göz ardı etmemizi sağlar fakat döngüden bir çıkış sağlamaz.

1. **break Komutu :** Bir koşula bağlı olarak while ve for döngülerden çıkmak için yani döngüleri sonlandırmak için kullanılır. Program akışını döngünün düışındaki ilk kımuta atlatır.

2. **continue Komutu :** Döngü içerisinde o anki işlemin atlanması ve bir sonraki işlemden devam edilmesini sağlar.


## İç İçe Döngüler :
Birden fazla döngü ve seçimli yapı iç içe kullanılabilir. Sırlama, matris veya tablo gibi iki-üç işlemlerin yapıldığı uygulamlarda sıklıkla iç içe döngüler kullanılır. İç içe döngülerin yapıları, bir döngü içersinde birden fazla döngünün kullanıldığı yapılardır. İçteki döngü tamamen bitmeden dıştaki döngü dıştaki döngüye gezilmez.

