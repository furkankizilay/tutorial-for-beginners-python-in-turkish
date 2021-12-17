import pandas as pd

dataset = pd.read_csv("USvideos.csv")

print(dataset.head(5)) # İlk 5 veriyi okur
print()
print("-----------------")
print()
print(dataset.drop(["thumbnail_link","video_id","trending_date","publish_time","thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed"],axis=1, inplace=True)) # Yazılan sütüları siler
print(dataset)
print()
print("-----------------")
print()
print(len(dataset.index)) # Kaç tane index olduğunu döndürür
print(len(dataset.columns)) # Kaç tane columns olduğunu döndürür
print()
print("-----------------")
print()
print(dataset["likes"].mean()) # Beğeni sayısnın ortalamsını bulur
print()
print("-----------------")
print()
print(dataset[dataset["views"] == dataset["views"].max()]["title"]) # En yüksek izlenmesi olan videonun başlığını döndürür
print()
print("-----------------")
print()
print(dataset[dataset["views"] == dataset["views"].min()]["title"]) # En düşük izlenmesi olan videonun başlığını döner
print()
print("-----------------")
print()
grup = dataset.groupby("category_id")
print(grup["comment_count"].mean()) # Kategorielre göre yorum sayılarının ortlamasını bulur
print()
print("-----------------")
print()
print(dataset["category_id"].value_counts()) # Kategorilerde kaç adet video olduğunu bulur
print()
print("-----------------")
print()
print(dataset["title"].apply(len)) # Her videounun başlık uzunluğunu içeren ekran çıktısı verir
print()
print("-----------------")
print()
dataset["title_lenght"] = dataset["title"].apply(len) # Videoların başlık uzunluğunun olduğu bir sütün eklendi
print(dataset)
print()
print("-----------------")
print()
def countTag(tag) :
    tagList = tag.split("|")
    return len(tagList)
print(dataset["tags"].apply(countTag)) # Bir videouda kaç tane tag kullanıldığını hesaplayan fonksiyonu databse'e gönderdik
dataset["tag_counts"] = dataset["tags"].apply(countTag) # Bir videouda kaç etiket olduğunu yeni bir sütün olarak database'e ekler
print(dataset)
print()
print("-----------------")
print()
print(list(dataset["likes"].iteritems())) # iter herbir indexi ve o index'e karşılık gelen değeri alarak bir tuple'a yerleştiriyor
likeslist = []
for key,value in list(dataset["likes"].iteritems()) : # Sadece beğeni sayılarını bir liste halinde aldık
    likeslist.append(value)
print(likeslist)
print()
print("-----------------")
print()
def likesdislikesratio(likes,dislikes) :
    likeslist = []
    for key, value in list(likes.iteritems()):
        likeslist.append(value)
    dislikeslist = []
    for key, value in list(dislikes.iteritems()):
        dislikeslist.append(value)

    likedislike = list(zip(likeslist,dislikeslist))
    ratio = []
    for like,dislike in likedislike :
        if (like + dislike) == 0 :
            ratio.append(0)
        else :
            ratio.append(like / (like+dislike))
    return ratio
dataset["likes_dislikes"] = likesdislikesratio(dataset["likes"],dataset["dislikes"])
print(dataset)
print("-----------------")
print()
#print(dataset.sort_values("likes_dislikes",ascending=False,inplace=True)) # Büyükten küçüğe sıralama



















