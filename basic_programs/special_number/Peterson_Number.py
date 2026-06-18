# Sum of factorial of digits = original number
# 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145number = int(input("Enter number: "))
number = int(input("Enter number: "))
temp = number
sum = 0

while number > 0:
    digit = number % 10
    fact = 1

    for i in range(1, digit+1):
        fact = fact * i
    sum = sum + fact
    number = number // 10

if temp == sum:
    print("Peterson Number")
else:
    print("Not Peterson Number")