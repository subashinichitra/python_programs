array= [10,-5,20,-3,8]
positive = 0
negative = 0
for i in array:
    if i > 0:
        positive = positive + 1
    elif i < 0:
        negative = negative + 1
print("Positive =", positive)
print("Negative =", negative)