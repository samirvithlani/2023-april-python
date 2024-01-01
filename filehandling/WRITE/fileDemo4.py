#write data in file:

#file = open("filehandling/demo1.txt","a") #open file in write mode

with open("filehandling/product.txt","a") as file:
    file.writelines("Hi this is new line\n this is second line\n this is third line\n")
    file.close()



users = ["hi this is my data\n","this is second line\n","this is third line\n"]
with open("filehandling/users.txt","a") as file:
    file.writelines(users)
    file.close()
    


    
    
    
    