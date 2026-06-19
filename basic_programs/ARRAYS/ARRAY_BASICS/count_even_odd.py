arr = [1,2,3,4,5,6]
even = 0
odd = 0

for i in arr:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Even Count =", even)
print("Odd Count =", odd)