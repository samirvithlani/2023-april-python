#Lambda function demo 1

# def printa(a):
#     return a + 10
# x = printa(10)
# print(x)

#printA(10)

x = lambda a : a + 10
print(x(10))

avg = lambda a,b,c : (a+b+c)//3
print(avg(100,200,300))


# def convert(name):
#     return name.upper()

# c = convert("python")
# print(c)

c = lambda name : name.upper()
print(c("python"))

#if else in lambda

# def checkeven(a):
#     if a %2 ==0:
#         return True
    
#     return False

# ce = checkeven(11)
# print(ce)



ce = lambda a : True if a %2 ==0 else False
print(ce(110))

# def findBigger(a,b):
#     if a > b:
#         return a
    
#     return b

# fb = findBigger(10,20)
# print(fb)


fb = lambda a,b : a if a>b else b
print(fb(100,20))

#10,20,30
def getHigher(a,b,c):
    # 10 > 20 and 10 > 30
    if a > b and a > c:
        return a
    #  20 > 30
    elif b > c:
        return b
    else:
        return c


gh = getHigher(101,20,30)
print(gh)



gh1 = lambda a,b,c : a if a>b and a > c else b if b > c else c
print(gh1(101,200,30))

# palindrome name using lambda... naman naman  madam malayalam

# def checkRev(name):
#     temp = name[::-1]
#     if temp == name:
#         return True
#     else:
#         return False

# flag = checkRev("nama")    
# print(flag)


    
chrev = lambda name : True if name[::-1] == name else False
print(chrev("naman"))



# def isValid(data,l,ch):
#     data = data.strip() #it will unneccessary space
#     if len(data) >=l and data.startswith(ch):
#         return True
#     else:
#         return False

# flag1 = isValid("  amita  ",5,"m")    
# print(flag1)


isValid = lambda data,l, ch : True if data.strip().startswith(ch) and len(data.strip())>=l else False
print(isValid("  amita  ",5,"a"))


#calling lambda function
#lambda a : print(a)(10)


