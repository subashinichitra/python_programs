n= int(input("ENTER THE NUMBER:"))
prime=[]
for num in range(2,n+1):
    for i in range(2,num):
        if num % i ==0:
            break
    else:
        prime.append(num)
for i in range(len(prime)-1):
    if prime[i+1]-prime[i]==2:
        print(prime[i],prime[i+1])
