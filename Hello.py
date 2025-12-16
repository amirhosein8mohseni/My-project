#tamrin1
print("hello word I happy")

 #Tamrin2
name = input("enter your name:")
print(f"hello {name} welcome to world")

#Tamrin3
temp = int(input("Enter air temp:"))
if temp > 30:
    print("air is hot")
else:
    print("air is not hot")

#Tamrin4
import time
for i in range(1,6):
    print(i)
    time.sleep(1)

#Tamrin5
numbers = [10,20,30]
print("List num")
for number in numbers:
    print(numbers)

#Tamrin6
def a(name):
    print(f"hello{name}welcome.")
    a("amir")

#Tamrin7
def say_hello(name):
    return f"سلام {name} از فایل utils!"

#tamrin8
from datetime import datetime

# گرفتن تاریخ و ساعت فعلی
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

# نوشتن در فایل
with open("log.txt", "w", encoding="utf-8") as file:
    file.write(f"زمان ثبت: {current_time}\n")
    file.write("این اولین لاگ من است!")

print("اطلاعات در فایل log.txt ذخیره شد")

#Tamrin9
import time
import signal
import sys

def signal_handler(sig, frame):
    print("\nبرنامه متوقف شد!")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

print("برنامه شروع شد. برای توقف Ctrl+C را بفشارید")

while True:
    print("برنامه در حال اجراست...")
    time.sleep(2)

#Tamrin10

