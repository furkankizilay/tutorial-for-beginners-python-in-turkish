import requests
import sys

url = "http://api.fixer.io/latest?base="

birinci_doviz = input("Birinci döviz :")
ikinci_döviz = input("İkinci döviz :")
miktar = float(input("Miktar :"))

response = requests.get(url + birinci_doviz) # birinci_döviz bilgileri çekildi

json_verisi = response.json() # internetten çekilen veri json formatına dönşür

try :
    print((json_verisi["rates"][ikinci_döviz]) * miktar)
except KeyError :
    sys.stderr.write("Lütfen para birimini doğru girin.")
    sys.stderr.flush() #büyük dosyalarda ekrana hemen yazak için kullanılır