import numpy as np
import pandas as pd
from numpy.random import randn

outerIndex = ["Group1","Group1","Group1","Group2","Group2","Group2","Group3","Group3","Group3"]
innerIndex = ["Index1","Index2","Index3","Index1","Index2","Index3","Index1","Index2","Index3"]

hierarchy=list(zip(outerIndex,innerIndex))
hierarchy=pd.MultiIndex.from_tuples(hierarchy)

df = pd.DataFrame(randn(9,3),hierarchy,columns=["C1","C2","C3"])
print(df)

print(df["C1"]) # C1'in adı ve dtype'i döner
print(df.loc["Group1"]) # Group1 değerleri döner
print(df.loc[["Group1","Group2"]]) # Group1 ve Group2 değerleri döner
print(df.loc["Group1"].loc["Index1"]) # Group1 deki Index1 değerlerini döner
print(df.loc["Group1"].loc["Index1"]["C1"])

print(df.xs("Group1"))
print(df.xs("Group1").xs("Index1"))
print(df.xs("Group1").xs("Index1").xs("C1"))

print(df.index.names)
df.index.names = ["Groups","Indexes"] # Indexlere dışardan başlayarak değer verdik
print(df)

df.xs("Index1",level ="Indexes") # indexlere değer verdi
print(df)