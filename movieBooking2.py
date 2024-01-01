file = open("movies2.txt", "r")

data = file.readlines()
#print(data)
#print(data)
movieDict = {}
for  i in data:
    movieMetaData = i.split(":")
    #print(movieMetaData)
    movieDict[movieMetaData[0]] = movieMetaData[1].strip("\n")

print(movieDict)    