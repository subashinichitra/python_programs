#sum of factorial of each digit = original number
#  1!  +  4!  +  5!  = 145
#  1   +  24  + 120  = 145
number = int(input("ENTER THE NUMBER: "))
temp= number
sum=0
while number>0:
    digits = number % 10
    fact=1
    for i in range(1,digits+1):
        fact = fact * i
    sum += fact
    number = number // 10
if sum == temp:
    print(f"{temp} is Strong number")
else:
    print(f"{temp} is  not a Strong number")



