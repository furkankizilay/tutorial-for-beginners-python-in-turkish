import numpy as np
import pandas as pd

df = pd.DataFrame({
    "Ay" : ["Mart","Nisan","Mayıs","Mart","Nisan","Mayıs","Mart","Nisan","Mayıs"],
    "Şehir" : ["Ankara","Ankara","Ankara","İstanbul","İstanbul","İstanbul","İzmir","İzmir","İzmir"],
    "Nem" : [10,25,50,21,67,80,90,70,75]

})

print(df)

#Indexler yerine ay bilgilerini Columnlar yerinede Şehir bilgilerini yazabiliriz.

print(df.pivot_table(index="Ay", columns="Şehir", values="Nem"))
