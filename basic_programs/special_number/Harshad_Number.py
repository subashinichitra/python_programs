# THE NUMBER WHICH IS DIVISIBLE BY SUM OF ITSELF
# STRING APPROACH
'''
number=int(input("ENTER THE NUMBER:"))
temp=str(number)
sum=0
for i in temp:
    sum = sum + int(i)
if number % sum == 0:
    print(f"{number} is Harshad Number ")
else: 
    print(f"{number} is not a Harshad Number")'''

# INTEGER + ARRAY APPROACH
n= int(input("ENTER THE TOTAL VALUES NEEDED:"))
arr=[]
for i in range(1,n+1):
    number=int(input("ENTER THE NUMBER:"))
    arr.append(number)

for j in arr:
    sum=0
    temp=j
    while j > 0:
        digits= j % 10
        sum = sum + digits
        j= j // 10
    if temp % sum == 0:
        print(f"{temp} is Harshad Number ")
    else: 
        print(f"{temp} is not a Harshad Number")