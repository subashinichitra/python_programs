arr = [10,20,30,40]
search = int(input("Enter search value: "))
flag = False
for i in arr:
    if i == search:
        flag = True
        break
if flag:
    print("Element Found")
else:
    print("Element  Is Not Found")