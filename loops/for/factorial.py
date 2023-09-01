#5 120 5 
no = int(input("Enter a number:"))
fact = 1
for i in range(1,no+1):
    #1 = 1 * 1 = 1
    #1 = 1 * 2 = 2
    #2 = 2 * 3 = 6
    #6 = 6 * 4 = 24 
    fact = fact * i

print("Factorial of ",no," is ",fact)    