# A number is Magic Number when repeatedly adding its digits finally gives 1.
# input: 19 => 1 + 9 => 10 => 1+0 => 1
number = int(input("Enter number: "))
while number > 9:
    sum = 0
    while number > 0:
        digit = number % 10
        sum = sum + digit
        number = number // 10
    number = sum

if number == 1:
    print("Magic Number")
else:
    print("Not Magic Number")