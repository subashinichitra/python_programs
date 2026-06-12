# without converting into string

number = int(input("ENTER THE NUMBER:"))
count = 0
while number > 0:
    count += 1
    number = number // 10
print(count)

#convert to string

number = input("ENTER THE NUMBER:")
count=0
for i in number:
    count+=1
print("TOTAL:",count)