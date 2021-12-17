import numpy as np
import pandas as pd

df = pd.DataFrame({

    "Column1" : [1,2,3,4,5,6],
    "Column2" : [100,100,200,300,300,100],
    "Column3" : ["Mustafa","Kamil","Emre","Ayşe","Murat","Zeynep"]
})

print(df)
print("--------------")

print(df.head(n=3)) #ilk 3 satırı verir default olarak ilk 5 satırı verir
print("--------------")

print(df["Column2"].unique()) # Column2'deki değerleri tekrarsız verir
print("----------------")

print(df["Column2"].nunique()) # Column2'de kaç farklı değer olduğunu döndürür
print("----------------")

print(df["Column2"].value_counts()) # Column2'de hangi değerden kaç tane olduğunu döndürür
print("----------------")

print(df[(df["Column1"] >= 4) & (df["Column2"]==300)])
print("----------------")

def times3(x) :
    return x * 3

print(df["Column2"].apply(times3))
print("---------------")

print(df["Column2"].apply(lambda x : x*2))
print("---------------")

print(df["Column3"].apply(len)) # Column3'deki her bir String'in herbir uzunluğunu verir
print("---------------")

print(df.drop("Column3", axis=1)) #Column3 geçici silinir
print("---------------")

print(df.columns) # Columnsarı tek satır halinde verir
print(df.index) # Indexlerin kaçtan başlayıp kaçta bittiğini söyler
print(df.index.names) # Indexlerin ismini verir
print("---------------")

print(df.sort_values("Column2")) # Küçükten büyüğe doğru sıralar
print(df.sort_values("Column2", ascending=False)) # Büyükten küçüğe doğru sıralanır
print("---------------")
