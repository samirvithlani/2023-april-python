
#convert string to uppercase
name = input("What is your name? ")

# print(ord('A'))
# print(chr(65))
lo_str=""
#amit
#m ascii = 109
for i in name:
    #asc = 97
    #asc = 109
    asc = ord(i)
    
    #true
    #true
    if asc>=97 and asc<=122:
        #"" = "" + "A"
        #A   ="A" +"M"
        #AM  ="AM" +"I"
        lo_str  = lo_str + chr(asc-32)


print(lo_str)        
    

      
        




        
    
#     if ord(name[i]>=97 and ord(name[i])<=122):
#         name[i] = ord(name[i]) - 32

# print(name)        
        



