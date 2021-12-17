import random
import string

def generate_password (lenght, level ,output = []) :
    chars = string.ascii_letters
    if level > 1 :
        chars = "{}{}".format(chars,string.digits)
    if level > 2 :
        chars = "{}{}".format(chars,string.punctuation)
    for i in range(lenght) :
        output.append(random.choice(chars))
    return "".join(output)

print(("-" * 30) + "\n Password Generator\n" + ("-" * 30))

password_lenght = int(input("Lenght :"))
password_level = int(input("Level :"))

password = generate_password(password_lenght,password_level)
print("\nYour password is : {}".format(password))