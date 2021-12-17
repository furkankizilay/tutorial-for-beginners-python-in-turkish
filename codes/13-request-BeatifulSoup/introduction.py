import requests # requests framework'ü ile verileri çekicez
from bs4 import BeautifulSoup #beatifulsopu framework'ü ile alıcağız

url = "https://tr.wikipedia.org/wiki/%C4%B0stanbul"

response = requests.get(url)

htm_içeriği = response.content

soup = BeautifulSoup(htm_içeriği,"html.parser")

#print(soup.prettify()) # sayfa kaynağının çıktısını verir

#print(soup.find_all("a")) # a etiketli kodları döner

'''for i in soup.find_all('a') :
    print(i)'''

'''for i in soup.find_all('a') : # linkleri döner
    print(i.get('href'))'''

'''for i in soup.find_all('a') :
    print(i.text)'''

for i in soup.find_all("div",{"class" : "thumb tright"}) :
    print(i)