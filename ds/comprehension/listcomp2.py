users = ["ram","ajay","jay","parth","sachin","saurav","dhoni","virat","rohit","rahul"]

fileusers = []

for i in users:
    if len(i)>3 and i.startswith("s"):
        fileusers.append(i)

print(fileusers)        

fileusers1 = [i for i in users if len(i)>3 and i.startswith("s")]

#fileusers1.pop()
print(fileusers1)