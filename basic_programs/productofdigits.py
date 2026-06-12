num=int(input("ENTER THE NUMBER: "))
temp=num
product=1

while num > 0:
    val= num % 10
    product= product * val
    num= num // 10

print(f"PRODUCT OF DIGITS FOR THIS NUMBER[{temp}] is {product} ")

