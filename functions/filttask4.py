def isalldigiteven(no):
    for i in no:
        if int(i) % 2 != 0:
            return False  # Return False if any digit is odd
    return True  # Return True if all digits are even

data = [22, 44, 57, 68, 28, 31, 39, 123, 222, 9099, 27]

x = list(filter(lambda no: isalldigiteven(str(no)), data))        
print(x)
