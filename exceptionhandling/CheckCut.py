
# from  InvalidString import InvalidString
# from  InvalidString import InvalidAge
from InvalidString import *

name = input("Enter your name: ")

try:
    if " " in name:
        raise InvalidString("No spaces allowed")
    
    print("Your name is: ", name)
except InvalidString as e:
    print(e)    
     