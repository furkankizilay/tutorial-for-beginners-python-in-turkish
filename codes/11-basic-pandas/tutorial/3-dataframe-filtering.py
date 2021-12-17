import numpy as np
import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(4,3),["A","B","C","D"],["Column1","Column2","Column3"])
print(df)
print(df>-1) # -1 den büyük olan değerleri True olarak döndürür
print(df[df>0]) # koşulu sağlayanlar aynen kalır sağlamayanalar nan değeri döndürür
print(df[df["Column1"]>0]) # Column1 de - değeri olan indexler ekran çıktısı olarak verilmez
print(df[(df["Column1"]>0)&(df["Column2"]>0)]) #and
print(df[(df["Column1"]>0)|(df["Column2"]>0)]) #or

df["Column4"] = pd.Series(randn(4),["A","B","C","D"]) # Column eklemenin bilinen yolu
df["Column5"] = randn(4) # Kısayolu
print(df)

df["Column6"] = ["newValue1","newValue2","newValue3","newValue4"]
print(df)

print(df.set_index("Column6")) # kaydedilmedi

df.set_index("Column6",inplace=True)
print(df)

print(df.index.names)
print(df.columns.names)