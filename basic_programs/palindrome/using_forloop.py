text = input("ENTER THE STRING: ")
reverse = ""
for i in text:
    reverse = i + reverse

if text == reverse:
    print("PALINDROME")
else:
    print("NOT A PALINDROME")