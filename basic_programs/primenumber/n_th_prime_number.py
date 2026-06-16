# what is the n th postion prime number ?n=int(input("ENTER THE NUMBER:"))

n=100
position= 8
a=[]
for num in range(2,n+1):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        a.append(num)
print(f"{position}th position value is " ,a[position-1])

    