num=int(input("ENTER THE NUMBER: "))
temp=num
sum=0

while num > 0:
    val= num % 10
    sum= sum + val
    num= num // 10

print(f"SUM OF DIGITS FOR THIS NUMBER[{temp}] is {sum} ")

