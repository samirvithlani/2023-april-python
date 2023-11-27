
try:
    no1 = int(input("Enter a number: "))
    no2 = int(input("Enter another number: "))
    #closing...

except ValueError:
    print("Invalid input")
    #closing...

finally:
    print("This will always execute")    
    no1 = None
    no2 = None
        