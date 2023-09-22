string="aello" 
ans="" 
#
for i in range(0,len(string)):
    # 97 and 122
    #a = 97 true
    if (ord(string[i]))>=97 and ord(string[i])<123:
        #"" + [a] ord 97 - 32   = 65 A
        #"A"
        ans+=chr(ord(string[i])-32)
    else:
        ans+=chr(string[i])
print(ans)