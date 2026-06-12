# FOR PARTICULAR NUMBER
number=int(input("ENTER THE NUMBER: "))
temp=number
sum=0
while number > 0:
    digits = number % 10
    sum= sum + (digits**3)
    number = number // 10

if temp == sum:
    print(f" {temp} IS ARMSTRONG")
else:
    print(f" {temp}  IS NOT A ARMSTRONG")


# PRINT 1 TO N
n = int(input("ENTER THE NUMBER: "))

for i in range(1, n + 1):

    temp = i
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum = sum + (digit ** 3)
        temp = temp // 10

    if i == sum:
        print(i)