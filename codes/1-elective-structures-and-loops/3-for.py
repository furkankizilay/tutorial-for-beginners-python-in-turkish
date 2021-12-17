# for (değişken) in range(5) range'in değerlerini sırayla değişkene atadı.
#for döngüsüde artık başka değer kalmadığı için alt satıra geçiş yapılır.
for index in range (1,6,2):
    print(f"{'*'*index:^9}")
print("Done")

#------------------------------
print()
for character in ["Furkan","Bahadır","Nesrin"]:
    print(character)

#-----------------------------
print() #enumerate hem sırası hemde stringi bastırmak istendiğinde kullanılır
for i, gun in enumerate(["pazar","pazartesi","salı","çarşamba","perşembe","cuma","cumartesi",]) :
    print(i,gun)

#-----------------------------
print()
numbers=[13,12,15,19,17,99,106]
çiftsayılarınToplamı=0
teksayılarınToplamı=0
for number in numbers:
    if number%2==0:
        print(f"{number} çift sayıdır.")
        çiftsayılarınToplamı+=number
    else:
        print(f"{number} tek sayıdır.")
        teksayılarınToplamı+=number

print(f"Çift sayıların toplamı {çiftsayılarınToplamı}'dır. ")
print(f"Tek sayıların toplamı {teksayılarınToplamı}'dır.")

#--------------------------
print() #yıgmalı toplama
#1-1/2+1/3-1/4+...........+-1/n
ST=0
sgn=1
n=int(input("Terim sayısı :"))
for x in range (1,1+n):
    ST=ST+(1/x)*sgn
    sgn=-sgn
print("Toplam :",ST)
#--------------------------
print()
for s1 in range(11):
    for s2 in range(11):
        print(f"{s1}*{s2}={s1*s2}")
    print()

#bir dögüde yatay ya da dikey satırların kaldırılması continue ile olur.
#--------------------------------
print()
for i in range (1,11):
    for j in range (1,11):
        print(i,"*",j,"=",i*j)
    print("")
#--------------------------------
print()
for a in [5,2,5,2,2]: #range kullanamayız çünkü düzenli artmıyor.
    print("X"*a)

#-------------------------
print()
for a in range(7,0,-1):
    for b in range(a,0,-1):
        print("*",end='')
    print("")

for i in range(7):
    for j in range(i+1):
        print("*",end='')
    print("")

#----------------------------
print()
index=1

while index<=9 :
    print(f'{"*"*index:^9}') #9,9 uzunluğunda bir stringe tamamla demek,^ ise ortala demek.
    index +=2