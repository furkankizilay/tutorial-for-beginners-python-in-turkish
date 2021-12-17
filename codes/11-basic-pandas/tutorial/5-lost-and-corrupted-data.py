import numpy as np
import pandas as pd
from numpy.random import randn

arr = np.array([[10,20,np.nan],[5,np.nan,np.nan],[21,np.nan,np.nan]])
#np.nan kayıp veri
df = pd.DataFrame(arr,index=["Index1","Index2","Index3"] ,columns=["Column1","Column2","Column3"])
print(df)

print(df.dropna()) #axis = 0 NaN olan indexleri siler
print()
print(df.dropna(axis=1)) #axis = 1 NaN olan Columnları siler
print()
print(df.dropna(thresh=2)) #Index'te Min 2 tane NaN yoksa silme
print()
print(df.fillna(value=1)) #NaN değerleri yerine 1 yaz
print()
print(df.sum()) #Columnların toplamı
print()
print(df.sum().sum()) #Columnların toplamının toplamı
print()
print(df.size) # Toplam kaç değer olduğunu döndürür
print()
print(df.isnull()) #Tüm DataFrame'de NaN olup olmadığını kontrol eder TRUE vey FALSE döner
print()
print(df.isnull().sum()) #Columnlarda Kaç tane NaN olduğunu döner
print()
print(df.isnull().sum().sum()) # kaç tane NaN olduğunu toplar
print()

def calculateMean(df):
    totalSum = df.sum().sum()
    totalNum = df.size - df.isnull().sum().sum()
    return totalSum / totalNum

print(calculateMean(df))

df.fillna(value=calculateMean(df),inplace=True)
print(df)
