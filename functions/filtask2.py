def the_str(i):
    if i.isalnum():
        return True
    else:
        return False 

data = ["ram sita", "asd1", "qwe qwe", "bleh1"]
x = list(filter(lambda i: the_str(i), data))
print(x)

#[22,31,123,46]
#even
#even