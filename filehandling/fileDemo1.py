#write data to file

#D:\projects\203-april-python\\demo.txt
#file = open("filehandling/demo1.txt","w") #open file in write mode
file = open("filehandling/demo1.txt","a") #open file in write mode
file.write("\nHello this is first line to write in file")
file.close() #close file

print("Data written successfully")
