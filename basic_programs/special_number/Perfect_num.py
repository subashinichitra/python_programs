# A NUMBER WHICH IS MULTIPLIED BY  THE SAME INTEGER = NUMBER
# 25 => 5 * 5 RIGHT
# 24 => 6 * 4 WRONG

n = int(input("ENTER THE NUMBER: "))
flag= False
for i in range(1,n):
    if i * i == n:
        flag=True
        break
if flag:
    print("PERFECT NUMBER")
else:
    print("NOT PERFECT NUMBER")
    