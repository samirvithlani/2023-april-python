def storeData(*args):
    
    def convertData(*args):
        # dataList = list(args)
        # return [i.upper() for i in dataList]
        return [i.upper() for i in  list(args)] 
    
    return convertData(*args)


x = storeData('a', 'b', 'c', 'd', 'e')
print("x -",x)
