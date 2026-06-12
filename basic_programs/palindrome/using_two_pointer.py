#USING TWO POINTER TO CHECK WHETHER IT IS PALINDROME OR NOT

text = input("ENTER THE STRING: ")

left = 0
right = len(text)-1

flag = True

while left < right:
    if text[left] != text[right]:
        flag = False
        break

    left += 1
    right -= 1

if flag:
    print("Palindrome")
else:
    print("Not Palindrome")