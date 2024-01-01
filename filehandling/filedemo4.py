try:
    file = open("abc.txt","x")
except FileExistsError:
    print("File already exists")    
