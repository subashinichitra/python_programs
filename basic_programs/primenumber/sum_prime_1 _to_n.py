n=int(input("ENTER THE NUMBER:"))
sum=0
for num in range(2,n+1):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        sum=sum+num
print(sum)` `