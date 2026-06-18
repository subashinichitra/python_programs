# If a number contains 0 inside it → Duck Number
# 1203= contains 0= Duck Number
number = input("Enter number: ")
flag = False

for i in number:
    if i == '0':
        flag = True
        break

if flag:
    print("Duck Number")
else:
    print("Not Duck Number")