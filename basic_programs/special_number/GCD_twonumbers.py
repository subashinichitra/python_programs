# GCD = Greatest number which divides both numbers.
# 12 and 18 => 12 → 1,2,3,4,6,12 18 → 1,2,3,6,9,18
#  common: 1,2,3,6    greatest => 6
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
gcd = 0

for i in range(1, min(a,b)+1):
    if a % i == 0 and b % i == 0:
        gcd = i
print("GCD =", gcd)