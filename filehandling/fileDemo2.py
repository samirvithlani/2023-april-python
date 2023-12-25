file = open("filehandling/demo1.txt","r") #open file in read mode

# data = file.read() #read all data from file
# print(data)

count = 0
for  i in file:
    count = count + 1
    print(i,end="")

print("Total lines in file are:",count)    