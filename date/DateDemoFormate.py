from datetime import date

today = date.today()

d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

d1 = today.strftime("%B %d, %Y")
print("d1 =", d1)

d1 = today.strftime("%m/%d/%y")
print("d1 =", d1)

d1 = today.strftime("%b-%d-%Y")
print("d1 =", d1)