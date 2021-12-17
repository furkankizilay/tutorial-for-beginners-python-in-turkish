def wordcount () :
    text = input("Type some text :")
    a = int(text.count(" "))
    b = a+1
    c = (len(text)-a)
    print(f"Text have {b} words.")
    print(f"Text have {c} letter.")

wordcount()