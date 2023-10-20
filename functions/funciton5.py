def printList(users):
    for i in users:
        print(i)


printList([10,20,30,40,50])        

def  filterList(data):
    for i in data:
        if i>30:
            print("iii",i)


filterList([100,20,30,31,29,89])            



def filList2(data):
    fdata=[]
    for i in data:
        if i.startswith('s'):
            fdata.append(i)
    
    return fdata


x = filList2(["sachin","ram","shyam","suresh","ramesh"])
print(x)        
    
def fillist3(data):
    return [i for i in data if i.startswith('s')]    


x1 = fillist3(["sachin","ram","shyam","suresh","ramesh"])
print(x1)
