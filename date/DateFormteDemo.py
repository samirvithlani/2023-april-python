from datetime import datetime

now = datetime.now()
print(now)

b1 = now.strftime("%d/%m/%Y %H:%M:%S")
print("b1 =", b1)

#12hour format

b1 = now.strftime("%d/%m/%Y %I:%M:%S %p %A %Z")
print("b1 =", b1)

#week Day.. print day name
#timezone


