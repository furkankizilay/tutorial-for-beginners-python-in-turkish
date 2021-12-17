import numpy as np
import pandas as pd
from numpy.random import randn

df = pd.DataFrame(data=randn(3,3),index=["A","B","C"],columns=["Column1","Column2","Column3"])
print(df)

print(df["Column1"]) #Column1'i verir
print(df[["Column1","Column3"]]) # 2 kapalı parantez kullandık !!!
print(df.loc["A"]) # A satırnı verir
print(df.iloc[0]) # yukarıdakiyle aynı sonucu verir
print(df.loc["A","Column1"]) # A indexinin column1 deki değerini döndürür
print(df.loc[["A","B"],["Column1","Column2"]])

df["Column4"] = pd.Series(data=randn(3),index=["A","B","C"]) # index'in aynı olması lazım !!!
print(df)

df["Total"] = df["Column1"]+df["Column2"]+df["Column3"]+df["Column4"] # aynı satırdaki değerle toplandı
print(df)

#df.drop("Total") bu kod hata alır çünkü axis belirtmedik
df.drop("Total",axis=1) #column axis'i 1 dir.
print(df) #herhangi bir değişkil omaz çğnkü drop işlemini kaydetmedik
df.drop("Total",axis=1,inplace=True) #kaydedildi
print(df)

