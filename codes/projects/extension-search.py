import os

os.walk("C:/Users")
pdf_dosyaları = list()
txt_dosyaları = list()
mp4_dosyaları = list()

for klasör_yolu, klasör_ismi, dosya_ismi in os.walk("C:/Users"):
    for i in dosya_ismi:
        if i.endswith(".pdf"):
            pdf_dosyaları.append(i)
        elif i.endswith(".mp4"):
            mp4_dosyaları.append(i)
        elif i.endswith(".txt"):
            txt_dosyaları.append(i)

with open("pdf_dosyaları.txt", "w", encoding="UTF-8") as file:
    for i in pdf_dosyaları:
        file.write(i + "\n")
with open("mp4_dosyaları.txt", "w", encoding="UTF-8") as file2:
    for i in mp4_dosyaları:
        file2.write(i + "\n")
with open("txt_dosyaları.txt", "w", encoding="UTF-8") as file3:
    for i in txt_dosyaları:
        file3.write(i + "\n")




