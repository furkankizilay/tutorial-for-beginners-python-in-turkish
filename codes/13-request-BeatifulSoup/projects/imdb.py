'''import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"

response = requests.get(url)

html_içeriği = response.content

soup = BeautifulSoup(html_içeriği, "html.parser")

a = float(input("Rating giriniz :"))

basliklar = soup.find_all('td',{"class" : "titleColumn"})
ratingler = soup.find_all('td', {'class' : 'ratingColumn imdbRating'})

for baslik,rating in zip(basliklar,ratingler) :
    baslik = baslik.text
    rating = rating.text

    baslik = baslik.strip() # baştaki ve sonraki boşlulalrı silicek
    baslik = baslik.replace("\n"," ")
    rating = rating.strip()
    rating = rating.replace("\n","")

    if (float(rating) >= a) :
        print(f"Film ismi : {baslik}, Film ratingi : {rating}")
'''
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"

response = requests.get(url)

icerik = response.content

soup = BeautifulSoup(icerik,"html.parser")

a = float(input("Min imdb puanını giriniz :"))

basliklar = soup.find_all("td",{"class" : "titleColumn"})
ratingler = soup.find_all("td", {"class" : "ratingColumn imdbRating"})

for baslik,rating in zip(basliklar,ratingler) :
    baslik = baslik.text
    rating = rating.text

    baslik = baslik.strip()
    baslik = baslik.replace("\n","")
    rating = rating.strip()
    rating = rating.replace("\n","")

    if (float(rating) >= a ) :
        print(f"Film adı : {baslik} -- imdb Puanı : {rating}")















