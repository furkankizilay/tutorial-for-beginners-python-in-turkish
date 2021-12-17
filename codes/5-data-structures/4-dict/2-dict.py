dictionary={
    "this":[("zamir","bu")], #kodlaması kolay olsun diye hepsini listeye dönüştürdük
    "is":[("fiil","olmak")],
    "a":[("belirteç","bir")],
    "book":[("isim","kitap"),("fiil","rezerve etmek")],
    "pen":[("isim","kalem")]
}
while True:
    sentence=input("Bir cümle giriniz : (Çıkış yapmak için ENTER'a basınız.)")
    if sentence=="":
        break
    for signCharacter in ".,=()[]{}:;":
        sentence=sentence.replace(signCharacter,"") #sentencedeki sign'ları boşluğa çevirdik.
    words=set(sentence.lower().split()) #split boşlukalarla ayrılmış kelimeleri lsite haline dönştürür. #set'e dönüştürdük çünkü bir kelime iki kez kullanılmasın diye.
    wordMaxLenght=1
    for word in words:
        if wordMaxLenght<len(word):
            wordMaxLenght=len(word)
    for word in words:
        wordDefinitions=dictionary.get(word,"Kelime bulunamadı.")
        if word not in dictionary:
            print(f"Girdiğiniz {{{word}}} kelimesi sistemde mevcut değildir. ")
            continue
        if len(wordDefinitions)==1:
            print(f"{word.upper():<{wordMaxLenght}}:({wordDefinitions[0][0]:^8}){wordDefinitions[0][1]}") #<{wml} sola dayalı düzenler #definition 0'dan sonra 8 boşlukluk koyar.
        elif len(wordDefinitions)>1:
            print(f"{word.upper():<{wordMaxLenght}}:" ,end="")
            for wordDefinition in wordDefinitions:
                print(f"({wordDefinitions[0]}){wordDefinitions[1]}",end="")
            print()
    print() #tekrar'ı bir alt satırda sorsun diye

print("Kullanıcı çıkışı yapıldı.")

#-----------------------------------------
print()
customer={
    "name":"furkan",
    "phone":"05419242095"

}
customer["name"]="bahadır" #köşeli parantez ile dict'de değişiklik yapabiliyoruz
print(customer)
customer["customerId"]=123456789
print(customer)
if "date" in customer: #date key'ı yok ama hata almak istemiyoruz.
    print(customer)
for key in customer: #dict'deki verilerin hepsine erişmek için for kullanılır.
    print(key)
for key in customer:
    print(f"{key}={customer[key]}")


digitMapping={"0":"Sıfır","1":"Bir","2":"İki","3":"Üç"}

number=(input("Enter a number :"))

outputString=""

for digit in number:
    outputString += f"{digitMapping.get(digit, '*')} "
print(outputString)

#-------------------------------------------
print()
bad_words=["amk","aq"]

sentence=input("Bir cümle giriniz :")

words=sentence.split()
string=""
for word in words:
    if word in bad_words:
        string=string+"."
    else:
        string=string+f"{word} "

print(string)