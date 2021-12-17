import time
import datetime

print("Please type your text after 3 seconds.")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("Go")
time.sleep(0.2)

before = datetime.datetime.now()
text = input("Type here :")
after = datetime.datetime.now()

speed = after - before
seconds = round(speed.total_seconds(),3)
letter_per_second = round(len(text) / seconds, 3)

print(f"You type in : {seconds} seconds.")
print(f"{letter_per_second} letters per seconds.")