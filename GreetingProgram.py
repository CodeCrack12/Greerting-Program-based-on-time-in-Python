# A Python Program Capable of Greeting You With Good Morning, Good Afternoon, Good Evening And Good Night Using time Module

from time import *

hours = strftime("%H:%M:%S")
print("The Time is : ", hours, "\n")
if hours >= "21:00:00":
    print("Good Night.")
elif hours >= "18:30:00":
    print("Good Evening.")
elif hours >= "12:00:00":
    print("Good AfterNoon.")
elif hours >= "05:00:00":
    print("Good Morning.")
elif hours >= "01:00:00":
    print("Good Night.")
input("\nPress Enter To Exit.")
