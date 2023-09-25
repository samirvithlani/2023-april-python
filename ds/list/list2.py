marks = [78,67,55,69,45,99,78]

print(marks)

cnt = marks.count(78)

# if cnt>0:
#         marks.remove(78)
# else:
#     print("not found") 

print("cnt===>",cnt)
# marks.sort()
# marks.reverse()

marks.sort(reverse=True)

print("after sorting")

for i in marks:
    print(i)



maxmarks = max(marks)
print("maxmarks===>",maxmarks)    