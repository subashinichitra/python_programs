# Square of the number ends with the same number
# 5 = 25
n=int(input("ENTER THE TOTAL NUMBER PRESENT IN ARRAY:"))
array=[]

for i in range(n):
    numbers=int(input())
    array.append(numbers)

for i in array:
    temp=i
    square=0
    square= i * i
    square= square % 10
    temp=temp % 10

    if temp == square:
        print(f"{i} IS AUTOMORPHIC NUMBER")
    else:
        print(f"{i} IS NOT AUTOMORPHIC NUMBER")


    