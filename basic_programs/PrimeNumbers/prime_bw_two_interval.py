starting=int(input("ENTER THE STARTING NUMBER:"))
ending=int(input("ENTER THE ENDING NUMBER:"))
for num in range(starting,ending+1):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(num)