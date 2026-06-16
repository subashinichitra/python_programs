start=int(input("ENTER THE STARTING NUMBER:"))
end=int(input("ENTER THE ENDING NUMBER:"))
for num in range(start,end+1):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(num)