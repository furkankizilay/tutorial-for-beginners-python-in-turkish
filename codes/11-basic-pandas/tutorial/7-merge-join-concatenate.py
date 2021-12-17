#İki DataFrame'i ister index'e göre ister column'a göre birbirine ekeleyebiliyoruz

import numpy as np
import pandas as pd

dataset1 = {
    "A" : ["A1","A2","A3","A4"],
    "B" : ["B1","B2","B3","B4"],
    "C" : ["C1","C2","C3","C4"]

}

dataset2 = {
    "A": ["A5", "A6", "A7", "A8"],
    "B": ["B5", "B6", "B7", "B8"],
    "C": ["C5", "C6", "C7", "C8"]

}

df1 = pd.DataFrame(dataset1, index= [1,2,3,4])
df2 = pd.DataFrame(dataset2, index= [5,6,7,8])

print(df1)
print(df2)

print(pd.concat([df1,df2])) # indexlere göre toplandı
print(pd.concat([df1,df2],axis=1)) # columnlara göre toplandı NaN değerler geldi

#------------------------------
#JOİN
#Left Join = (A U B) - (B - A) ----- (A + A N B )
# indexlere göre
dataset3 = {
    "A" : ["A1","A2","A3","A4"],
    "B" : ["B1","B2","B3","B4"]

}

dataset4 = {
    "X" : ["X1","X2","X3"],
    "Y" : ["Y1","Y2","Y3"]

}

df3 = pd.DataFrame(dataset3, index= [1,2,3,4])
df4 = pd.DataFrame(dataset4, index= [1,2,3])

print(df3.join(df4)) #df3'ün indexleri geldi
print(df4.join(df3)) #df4'ün indexleri geldi


#-------------------------------------
#Marge
# A N B
#Columnlara göre

dataset5 = {
    "A" : ["A1","A2","A3"],
    "B" : ["B1","B2","B3"],
    "anahtar" : ["K1","K2","K3"]

}

dataset6 = {
    "X" : ["X1","X2","X3","X4"],
    "Y" : ["Y1","Y2","Y3","Y4"],
    "anahtar" : ["K1","K2","K3","K4"]

}

df5 = pd.DataFrame(dataset5, index=[1,2,3])
df6 = pd.DataFrame(dataset6, index=[1,2,3,4])

print(pd.merge(df5,df6,on = "anahtar")) #anahtar değerlerinden ortakl olanalra göre inner işlemi yapar
