#  SUM OF THE DIGITS= PRODUCT OF THE DIGITS

# STRING BASED
number=input("ENTER THE NUMBER:")
sum=0
product=1
for i in number:
    sum = sum + int(i)
    product = product * int(i)
if sum == product:
    print(f"{number} IS SPY NUMBER")
else:
    print(f"{number} IS NOT SPY NUMBER")

# INTEGER BASED
number=int(input("ENTER THE NUMBER:"))
temp= number
sum=0
product=1
while number > 0:
    digits = number % 10
    sum = sum + digits
    product = product * digits
    number=number // 10
if sum == product:
    print(f"{temp} IS SPY NUMBER")
else:
    print(f"{temp} IS NOT SPY NUMBER")
