number=int(input("ENTER THE PALINDROME NUMBER: "))
temp=number
reverse=0
while number > 0:
    digits = number % 10
    reverse = reverse * 10 + digits
    number = number // 10

if temp == reverse:
    print(f" {temp} IS PALINDROME")
else:
    print(f" {temp}  IS NOT A PALINDROME")


