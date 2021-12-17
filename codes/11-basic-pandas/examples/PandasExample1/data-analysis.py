import pandas as pd

dataset = pd.read_csv("mls-salaries-2017.csv")

print(dataset.head(n = 10)) # İlk 10 veriyi okur
print()
print("-----------------")
print()
print(len(dataset.index)) # Kaç tane index olduğunu döndürür
print()
print("-----------------")
print()
print(dataset["base_salary"].sum()/len(dataset.index))# Maaşların ortalamasını bulur
#print(dataset["base_salary"].mean())
print()
print("-----------------")
print()
print(dataset["base_salary"].max()) # En yüksek maaşı bulur
print()
print("-----------------")
print()
print(dataset["guaranteed_compensation"].max())
print()
print("-----------------")
print()
print(dataset[dataset["guaranteed_compensation"] == dataset["guaranteed_compensation"].max()]["last_name"]) # En yüksek tazminatlı oyuncunun adını bulur
print()
print("-----------------")
print()
print(dataset[dataset["last_name"] == "Gonzalez Pirez"]["position"]) # Adı verilen oyuncunun mevkisini döndürür
print()
print("-----------------")
print()
print(dataset.groupby("position").mean()) # Oyuncuları mevkielre göre sıraladı ve ortalma maşşları buldu
print()
print("-----------------")
print()
print(dataset["position"].nunique()) # Kaç farklı mevki olduğunu gösterir
print()
print("-----------------")
print()
print(dataset["position"].value_counts()) # Pozisyonlarda kaç farklı değer olduğunu bulur
print()
print("-----------------")
print()
print(dataset["club"].value_counts()) # Kaç klup olduğunu döndürür
print()
print("-----------------")
print()
def son_find(last_name) :
    if "son" in last_name.lower() :
        return True
    return False
print(dataset["last_name"].apply(son_find))
print()
print("-----------------")
print()
print(dataset[dataset["last_name"].apply(son_find)])





