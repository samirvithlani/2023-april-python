data =[1,2,3,4,5]
squares = []

for i in data:
    squares.append(i**2)

print(squares)    

#convert to comprehension

squares1 = [i**2 for i in data]
print(squares1)

#even numbers list comprehension


evenLisy =[i for i in range(1,11) if i % 2 ==0]