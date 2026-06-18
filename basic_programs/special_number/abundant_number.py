#Find factors except the number itself
#Add those factors
#If factor sum > number → Abundant numbernumber = int(input("Enter number: "))
number = int(input("Enter number: "))
sum = 0

for i in range(1, number):

    if number % i == 0:
        sum = sum + i


if sum > number:
    print("Abundant Number")
else:
    print("Not Abundant Number")