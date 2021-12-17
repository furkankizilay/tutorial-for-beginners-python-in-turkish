import numpy as np
import pandas as pd

#Arrayden farklı olarak index sütunu bulunur.

label_list = ["Furkan","Bahadır"]
data_list = [10,20]

print(pd.Series(data = data_list , index=label_list))
#data ile index'in eleman sayısı eşit olmalı

print(pd.Series(data= data_list))
#indexi kendisi 0 1 olarak verdi

npArray = np.array([1,2,3,4,5,6])
print(pd.Series(npArray))

print(pd.Series(data =npArray , index=["A","B","C","D","E","F"]))

dataDict = {"Kadir" : 30 , "Mustafa" : 40, "Ahmet" : 50}
print(pd.Series(dataDict))

ser2017 = pd.Series([5,10,15,20],["A","B","C","D"])
ser2018 = pd.Series([10,20,30,40],["A","B","F","D"])
total = ser2017+ser2018
print(total) # C ve F değerleri NaN
print(total["A"]) #15 değeri döner
print(total["C"]) #nan değeri döner
