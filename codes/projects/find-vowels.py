def vowels_count (text, output = 0) :
    vowels = "aeiouAEIOU"
    for char in text :
        if char in vowels :
            output +=1
    return output

text = input("Type some text :")
print("Vowels in text : {}".format(vowels_count(text)))