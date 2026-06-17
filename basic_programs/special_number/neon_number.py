# Sum of digits of its square = Original number
# 9 = 9 * 9 = 81 = 8 + 1 = 9

n=int(input("ENTER THE NUMBER:"))
sum=0
square = str (n * n)
for i in square:
    sum = sum + int(i)
if n == sum:
    print(f"{n} IS NEON NUMBER")
else:
    print(f"{n} IS NOT NEON NUMBER")


    