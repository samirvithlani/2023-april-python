#Raise keyword


age = int(input("Enter your age: "))

try:
    if age < 0:
        raise ValueError("Age can not be negative")
    
    print("Your age is: ", age)
except ValueError as e:
    print(e)    