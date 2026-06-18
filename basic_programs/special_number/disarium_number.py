#Sum of digits powered with their position = same number135
# 1¹ + 3² + 5³ = 1 + 9 + 125 = 135
number = int(input("Enter number: "))
temp = number
value = str(number)
length = len(value)
sum = 0

while number > 0:
    digit = number % 10
    sum = sum + (digit ** length)
    length = length - 1
    number = number // 10

if temp == sum:
    print("Disarium Number")
else:
    print("Not Disarium Number")