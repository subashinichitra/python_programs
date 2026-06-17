# sum of factors ( except last digit) = original number
#  1  +  2  +  3  =  6
number = int(input("ENTER THE NUMBER: "))
temp= number
sum=0
for i in range(1,number):
    if number % i == 0:
        sum= sum + i
if sum == temp:
    print(f"{temp} is Perfect number")
else:
    print(f"{temp} is  not a Perfect number")