
def prime(temp):
    for i in range(len(temp)):
        rotate=int(temp[i:]+temp[:i])
        print(rotate)

        for j in range(2,rotate):
            if rotate % j ==0:
                flag=1
                break

number=int(input("ENTER THE NUMBER: "))
temp=str(number)
flag=0
prime(temp)
if flag==0:
     print(f"THE GIVEN NUMBER {number} IS A CIRCULAR PRIME")
else:
    print(f"THE GIVEN NUMBER {number} IS NOT A CIRCULAR PRIME")