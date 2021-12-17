import numpy as np
import pandas as pd


dataset = {
    "Departman":["Bilişim","İnsan Kaynakları","Üretim","Üretim","Bilişim","İnsan Kaynakları"],
    "Çalışan":["Mustafa","Sinem","Ahmet","Burak","Mert","Yusuf"],
    "Maaş":[3000,5000,6000,7000,8000,1000]

}
df = pd.DataFrame(dataset)
print(df)
print("--------------------")

print(df.groupby("Departman").sum()) #Deaprtmandakilerin maaşını toplar
print("--------------------")
print(df.groupby("Departman").sum().loc["Bilişim"]) #Bilişimdeki toplam maaşı döndürür
print("--------------------")
print(df.groupby("Departman").count()) #Departmnalardaki çalışan ve maaş sayısını döndürür
print("--------------------")
print(df.groupby("Departman").max()) #Departmandaki max maaş ve alfabetik sıraya göre en büyük ismi döndürür
print("--------------------")
print(df.groupby("Departman").min()["Maaş"]) #Departmanlardaki en az maaşı döndürür
print("--------------------")
print(df.groupby("Departman").mean()["Maaş"]["İnsan Kaynakları"]) #İnsan Kaynaklarında çalışanların maaşlarının ortlamasını döndürür